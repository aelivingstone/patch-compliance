# Patch Compliance Analysis Reference Architecture

This reference architecture creates AWS Systems Manager Associations to [automatically update the SSM Agent](https://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-agent-automatic-updates.html), [configure inventory collection](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-inventory-configuring.html) and [run patching operations](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-about-aws-runpatchbaseline.html) for scanning and optionally installing. It also creates [maintenance windows](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-maintenance.html) for the optional installation of patches. A Lambda function generates Tags for PlatformType, PlatformName and PlatformVersion to enable a target for patching. AWS Config is also enabled in all regions and accounts provided.

The information from AWS Config and AWS Systems Manager Inventory is collected in S3 buckets in the deployment account and Athena Tables and Views are created to analyse the data using Amazon QuickSight. An AWS Lambda function [repairs](https://docs.aws.amazon.com/athena/latest/ug/msck-repair-table.html) the tables and creates an Athena datasource and two datasets for use in QuickSight, joining multiple tables for further insight. An additional AWS Lambda function is created to partition data from AWS Config.

## High Level Architecture

![Architecture Diagram](https://github.com/aelivingstone/patch-compliance/blob/master/images/Diagram.png)

## Motivation

Simplify installation, configuration and analysis of patch compliance information using data from AWS Config and AWS Systems Manager. Using data from AWS Config also allows for the analysis of unmanaged instances or instances that have been stopped or terminated. 

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
ConfigDeliveryChannel | StackSet-patch-compliance-Stackset-a80e2dfd-515d-4d45-a812-7956b0448688-ConfigDeliveryChannel-WQG3LXIYJX2N	
ConfigRecorder | StackSet-patch-compliance-Stackset-a80e2dfd-515d-4d45-a812-7956b0448688-ConfigRecorder-JBRZM5T3KHVV	
ConfigRecorderRole | StackSet-patch-compliance-Stack-ConfigRecorderRole-1AAVE31N71S9B	
ConfigTopic | arn:aws:sns:eu-west-1:180304385487:config-topic-180304385487	
ConfigTopicPolicy | StackSet-patch-compliance-Stackset-a80e2dfd-515d-ConfigTopicPolicy-14346OKPIL4ZW	
EC2Tagging | CustomResourcePhysicalID	
EC2TaggingFunction | StackSet-patch-compliance-Stack-EC2TaggingFunction-JVSP6OYIDRR3	
GatherSoftwareInventoryAssociation | bab94214-19cb-4a46-838e-25ecfd826bc3	
LambdaExecutionRole | StackSet-patch-compliance-Stac-LambdaExecutionRole-TTPJARPHC1SS	
PatchAWSSSMMaintenanceWindow | mw-080056c538ea063a0	
PatchAWSSSMMaintenanceWindowTarget | 1e423856-cd15-4314-baf4-1b8265ce939d	
PatchAWSSSMMaintenanceWindowTask | 37e5fcb2-f557-4f33-a0d1-e8c11179a550	
ResourceDataSync | patch-compliance-sync	
RunPatchBaselineAssociation | b8023097-416a-4e2b-a71c-a5129285150a	
UpdateSSMAgentAssociation | 037581d5-18fb-4d15-8a89-d1812f7d94cc

## Prerequisites
All instances must be managed.

## License Summary
This reference code is made available under the MIT-0 license. See the LICENSE file.
