# Patch Compliance Analysis Reference Architecture

This reference architecture creates AWS Systems Manager Associations to [automatically update the SSM Agent](https://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-agent-automatic-updates.html), [configure inventory collection](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-inventory-configuring.html) and [run patching operations](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-about-aws-runpatchbaseline.html) for scanning and optionally installing patches. It also creates [maintenance windows](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-maintenance.html) for the optional installation of patches. A Lambda function generates Tags for PlatformType, PlatformName and PlatformVersion to enable a target for patching. AWS Config is also enabled in all regions and accounts provided.

The information from AWS Config and AWS Systems Manager Inventory is collected in S3 buckets in the deployment account and Athena Tables and Views are created to analyse the data using Amazon QuickSight. An AWS Lambda function [repairs](https://docs.aws.amazon.com/athena/latest/ug/msck-repair-table.html) the tables, adds views and creates an Athena datasource and two datasets for use in QuickSight, joining multiple tables for further insight. An additional AWS Lambda function is created to partition data from AWS Config.

## High Level Architecture
![Architecture Diagram](https://github.com/aelivingstone/patch-compliance/blob/master/images/Diagram.png)

## Technologies
![Technologies Diagram](https://github.com/aelivingstone/patch-compliance/blob/master/images/Technology.png)

## Motivation
Simplify installation, configuration and analysis of patch compliance information using data from AWS Config and AWS Systems Manager. Using data from AWS Config also allows for the analysis of unmanaged instances or instances that have been stopped or terminated. 

## Features

* Multi-Account, Multi-Region Deployment of AWS Config
* Multi-Account, Multi-Region Deployment of AWS Systems Manager Association to automatically update AWS Systems Manager Agent
* Multi-Account, Multi-Region Deployment of AWS Systems Manager Association to configure inventory collection
* Multi-Account, Multi-Region Deployment of AWS Systems Manager Association to scan for patches
* Multi-Account, Multi-Region Deployment of Patch Maintenance Windows
* Multi-Account, Multi-Region Deployment of Patching Operations
* Multi-Account, Multi-Region Tagging of Managed EC2 instances with OS Details
* Centralised AWS Systems Manager Inventory Data
* Centralised AWS Config Data
* Automatic creation of Athena Tables and Views
* Automatic re-partitioning of AWS Config data
* Automatic creation of QuickSight data source and datasets

## Code Examples

### Lambda Function to tag EC2 Instances

```python
import boto3
import json
import logging
import cfnresponse

ssm = boto3.client('ssm')
ec2 = boto3.client('ec2')
logger = logging.getLogger()
logger.setLevel(logging.INFO)     

def handler(event, context): 
# set token to empty string
token = ''

# set response value to 0
responseValue = 0

while True:
    # Limit to 50 due to describe limit
    response = ssm.describe_instance_information(
        MaxResults=50,
        NextToken = token
    )
    
    for instanceInfo in response['InstanceInformationList']:
        # Create empty instances array
        instances = []                  
        instanceId = instanceInfo['InstanceId']
        logger.info('InstanceID: ' + instanceId)  
        instances.append(instanceId) 
        platformType = instanceInfo['PlatformType']
        logger.info('OS type: ' + platformType)
        osName = instanceInfo['PlatformName']
        logger.info('OS name: ' + osName)
        osVersion = instanceInfo['PlatformVersion']
        logger.info('OS version: ' + osVersion)
        logger.info('---')
        
        responseValue += 1
                            
        tagResponse = ec2.create_tags(
            Resources = instances,
            Tags = [
                {
                    'Key': 'PlatformType',
                    'Value': platformType
                },
                {
                    'Key': 'OSName',
                    'Value': osName
                },    
                {
                    'Key': 'OSVersion',
                    'Value': osVersion
                },                   
            ]
        )           
        
    if 'NextToken' not in response: break    
    token = response['NextToken']
    logger.info('Token: ' + token) 
responseData = {}
responseData['InstancesTagged'] = responseValue
cfnresponse.send(event, context, cfnresponse.SUCCESS, responseData, "CustomResourcePhysicalID")
```

### SQL to create Config Managed Instance Compliance View
```sql
CREATE OR REPLACE VIEW ConfigMIC AS 
    SELECT MAX(dt) as ConfigMICDate, 
        MAX(configurationItem.awsaccountid) as ConfigMICAccountID, 
        MAX(configurationItem.awsregion) as ConfigMICRegion, 
        split(configurationItem.resourceid,'/')[2] as ConfigMICInstanceID, 
        MAX(instance.tags['name']) as ConfigMICName,
        MAX(json_extract_scalar(instance.configuration, '$.state.name')) as ConfigMICState,
        MAX(json_extract_scalar(regexp_extract(configurationItem.configuration, '\\{[^}{.]*ec2-instance-managed-by-systems-manager[^}.]*\\}'), '$.compliancetype')) as ConfigMICComplianceStatus
    FROM patch_compliance.aws_config_snapshot 
        CROSS JOIN UNNEST(configurationitems) AS t1(configurationItem)
        CROSS JOIN UNNEST(configurationitems) AS t2(instance)
    WHERE regexp_like(configurationItem.configuration, '\\{[^}{.]*ec2-instance-managed-by-systems-manager[^}.]*\\}')
        AND configurationItem.resourcetype = 'AWS::Config::ResourceCompliance'
        AND t2.instance.resourceID = split(configurationItem.resourceid,'/')[2]
    GROUP BY split(configurationItem.resourceid,'/')[2]
```
## Prerequisites
* To gather data using AWS Systems Manager, the instance has to be a [Managed Instance](https://docs.aws.amazon.com/systems-manager/latest/userguide/managed_instances.html)
* AWS Systems Manager Inventory must not be enabled in target regions, the embedded Stackset will fail if it is enabled
* [Setup QuickSight](https://docs.aws.amazon.com/quicksight/latest/user/setup-quicksight-for-existing-aws-account.html)
* [Grant self-managed permissions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs-self-managed.html) for StackSets
* Target regions must be enabled, otherwise the embedded Stackset will fail. Check your regions using ```aws ec2 describe-regions | grep RegionName```
** See [Prerequisites for stack set operations](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs.html)

## Deployment Instructions
Everything is embedded in to the **patch-compliance.yml** CloudFormation template, apart from the AWS Lambda function to create the QuickSight data source and datasets. The parameters in the CloudFormation template will allow you to reference the location of the uploaded function.

1. Upload the AWS Lambda function **quicksight.zip** to an S3 Bucket in your administrator account
1. Deploy patch-compliance.yml using CloudFormation
1. Set QuickSight to [refresh your datasets on a schedule](https://docs.aws.amazon.com/quicksight/latest/user/refreshing-imported-data.html#schedule-data-refresh)

### Help with parameters
You can check your QuickSight User by hovering over your account icon in the top right corner or by clicking on the icon and selecting Manage QuickSight.

![QuickSight Users Screenshot](https://github.com/aelivingstone/patch-compliance/blob/master/images/quicksight_user.png)

You can retrieve your PrincipalOrgID by using the CLI command: `aws organizations describe-organization` or by going to **AWS Organizations** > **Organize accounts** where you'll see it in the ARN on the right-hand side in the format **o-xxxxxxxxxx**. This is used to provide the AWS Config service access to put objects in the central bucket.

Before you choose which regions to deploy to, check which regions are enabled by going to **My Account** and scrolling down to AWS Regions. Choosing a region that you do not have enabled will result in a failure. Or use the CLI command: ```aws ec2 describe-regions | grep RegionName```.

![Regions Screenshot](https://github.com/aelivingstone/patch-compliance/blob/master/images/regions.png)

## Preparing QuickSight for your Datasets
* Open QuickSight
* Choose **Datasets**, you should see something like this:

![QuickSight Datasets Screenshot](https://github.com/aelivingstone/patch-compliance/blob/master/images/quicksight_datasets.png)

* Click on **Patch Compliance Data Set**:

![QuickSight Patch Compliance Dataset Screenshot](https://github.com/aelivingstone/patch-compliance/blob/master/images/patch_compliance_data_set.png)

* Click on the **Create analysis** button
* You now have a blank analysis:

![QuickSight Blank Analysis Screenshot](https://github.com/aelivingstone/patch-compliance/blob/master/images/analysis.png)

* Click on the edit icon to the right of **Data Set**
* Click **Add data set**
* Select **Patch Compliance by Tag**
* Click **Select**
* In the drop down below **Data set** you can now choose which dataset to use for creating visualizations

## The Data
The two datasets are made up of a mixture of views and tables that have been left joined to the **configmic** view. This view contains all the instances in all the accounts and regions along with whether or not it's compliance status as a managed instance is compliant or not (configmiccompliancestatus) as per the **ec2-instance-managed-by-systems-manager** check in AWS Config. 
* [https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-inventory-schema.html](AWS Systems Manager Inventory Schema)
* [AWS Config Schema](https://github.com/awslabs/aws-config-resource-schema)

The **configpc** view contains the same instances and whether or not they are compliant (configpcstatus) with patching as per the **ec2-managedinstance-patch-compliance-status-check** in AWS Config. This is useful because it will continue to show the compliance status, even if the instance has been stopped. The latest data from Systems Manager will not include data from stopped instances.

The **Patch** view is a filtered version of the **aws_compliance_item** where the compliance type is equal to **patch**. This is included because the QuickSight API does not currently support creating view using custom SQL queries. This data is from Systems Manager and contains information about each patch related to the instance.

All of the other Athena tables represent data from Systems Manager. Not all of them are included in the datasets, but they have been included so that you can query directly against them in Athena or create your own datasets.

The reason for creating multiple datasets is because joining many tables with a one to many relationship creates massive temporary tables that would timeout beyond all but the smallest data sets. 

The first data set contains information about the instances and their patching status to an individual patch level. Because this uses Sysems Manager data, you cannot display individual patch data about instances that are stopped:

![Patch Compliance Data Set Joins Screenshot](https://github.com/aelivingstone/patch-compliance/blob/master/images/patch_compliance_data_set_joins.png)

The second data set just contains the compliance data from AWS Config, joined with instance tags, this allows you to create visualizations on patching and managed instance compliance based on tag keys and values so that you can view compliance based on owner, business unit,  workload, stack or whatever you are using for tagging.

![Patch Compliance by Tag Data Set Joins Screenshot](https://github.com/aelivingstone/patch-compliance/blob/master/images/patch_compliance_by_tag_dataset_joins.png)

## Resources Created in Deployment Account
Logical ID | Type
---------- | ----
AthenaAWSComponentTable | AWS::Glue::Table
AthenaApplicationTable | AWS::Glue::Table
AthenaBucket | AWS::S3::Bucket
AthenaComplianceItemTable | AWS::Glue::Table
AthenaConfigMICVNamedQuery | AWS::Athena::NamedQuery
AthenaDatabase | AWS::Glue::Database
AthenaInstanceDetailedInformationTable | AWS::Glue::Table
AthenaInstanceInformationTable | AWS::Glue::Table
AthenaNetworkTable | AWS::Glue::Table
AthenaPatchSummaryTable | AWS::Glue::Table
AthenaResourceGroupTable | AWS::Glue::Table
AthenaServiceTable | AWS::Glue::Table
AthenaTable | AWS::Glue::Table
AthenaTagTable | AWS::Glue::Table
AthenaWindowsRoleTable | AWS::Glue::Table
AthenaWindowsUpdateTable | AWS::Glue::Table
ConfigAggregator | AWS::Config::ConfigurationAggregator
ConfigAggregatorRole | AWS::IAM::Role
ConfigBucket | AWS::S3::Bucket
ConfigBucketPolicy | AWS::S3::BucketPolicy
CustomResourceLambdaFunction | AWS::Lambda::Function
DataSyncBucket | AWS::S3::Bucket
DataSyncBucketPolicy | AWS::S3::BucketPolicy
LambdaExecutionRole | AWS::IAM::Role
LambdaIAMRole | AWS::IAM::Role
LambdaInvokePermission | AWS::Lambda::Permission
LambdaTrigger | Custom::LambdaTrigger
PartitioningFunction | AWS::Lambda::Function
QuickSight | Custom::Function
QuickSightFunction | AWS::Lambda::Function
QuicksightLambdaExecutionRole | AWS::IAM::Role
StackSet | AWS::CloudFormation::StackSet

## Resources Created in Target Accounts and Regions
Logical ID | Type
---------- | ----
ConfigDeliveryChannel | AWS::Config::DeliveryChannel	
ConfigRecorder | AWS::Config::ConfigurationRecorder	
ConfigRecorderRole | AWS::IAM::Role	
ConfigTopic | AWS::SNS::Topic	
ConfigTopicPolicy | AWS::SNS::TopicPolicy	
EC2Tagging | Custom::Function	
EC2TaggingFunction | AWS::Lambda::Function	
GatherSoftwareInventoryAssociation | AWS::SSM::Association	
LambdaExecutionRole | AWS::IAM::Role	
PatchAWSSSMMaintenanceWindow | AWS::SSM::MaintenanceWindow	
PatchAWSSSMMaintenanceWindowTarget | AWS::SSM::MaintenanceWindowTarget	
PatchAWSSSMMaintenanceWindowTask | AWS::SSM::MaintenanceWindowTask	
ResourceDataSync | AWS::SSM::ResourceDataSync	
RunPatchBaselineAssociation | AWS::SSM::Association	
UpdateSSMAgentAssociation | AWS::SSM::Association	

## License Summary
This reference code is made available under the MIT-0 license. See the LICENSE file.
