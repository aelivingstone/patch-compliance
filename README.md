# Patch Compliance Analysis Reference Architecture

This reference architecture creates AWS Systems Manager Associations to [automatically update the SSM Agent](https://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-agent-automatic-updates.html), [configure inventory collection](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-inventory-configuring.html) and [run patching operations](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-about-aws-runpatchbaseline.html) for scanning and optionally installing. It also creates [maintenance windows](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-maintenance.html) for the optional installation of patches. A Lambda function generates Tags for PlatformType, PlatformName and PlatformVersion to enable a target for patching. AWS Config is also enabled in all regions and accounts provided.

The information from AWS Config and AWS Systems Manager Inventory is collected in S3 buckets in the deployment account and Athena Tables and Views are created to analyse the data using Amazon QuickSight. An AWS Lambda function [repairs](https://docs.aws.amazon.com/athena/latest/ug/msck-repair-table.html) the tables, adds views and creates an Athena datasource and two datasets for use in QuickSight, joining multiple tables for further insight. An additional AWS Lambda function is created to partition data from AWS Config.

## High Level Architecture
![Architecture Diagram](https://github.com/aelivingstone/patch-compliance/blob/master/images/Diagram.png)

## Technologies
![Technologies Diagram](https://github.com/aelivingstone/patch-compliance/blob/master/images/Technology.png)

## Motivation
Simplify installation, configuration and analysis of patch compliance information using data from AWS Config and AWS Systems Manager. Using data from AWS Config also allows for the analysis of unmanaged instances or instances that have been stopped or terminated. 

## Features

## Code Example
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

## Deployment Instructions

### Help with parameters
You can check your QuickSight User by hovering over your account icon in the top right corner or by clicking on the icon and selecting Manage QuickSight.
![QuickSight Users Screenshot](https://github.com/aelivingstone/patch-compliance/blob/master/images/quicksight_user.png)

You can retrieve your PrincipalOrgID by using the CLI command: `aws organizations describe-organization` or by going to **AWS Organizations** > **Organize accounts** where you'll see it in the ARN on the right-hand side in the format **o-xxxxxxxxxx**. 

Before you choose which regions to deploy to, you may want to check whch regions are enabled by going to **My Account** and scrolling down to AWS Regions. Choosing a region that you do not have enabled will result in a failure.
![Regions Screenshot](https://github.com/aelivingstone/patch-compliance/blob/master/images/regions.png)



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

## Prerequisites
All instances must be managed.

## License Summary
This reference code is made available under the MIT-0 license. See the LICENSE file.
