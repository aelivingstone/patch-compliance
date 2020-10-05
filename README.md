# Patch Compliance Analysis Reference Architecture

This reference architecture creates AWS Systems Manager Associations to [automatically update the SSM Agent](https://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-agent-automatic-updates.html), [configure inventory collection](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-inventory-configuring.html) and [run patching operations](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-about-aws-runpatchbaseline.html) for scanning and optionally installing. It also creates [maintenance windows](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-maintenance.html) for the optional installation of patches. A Lambda function generates Tags for PlatformType, PlatformName and PlatformVersion to enable a target for patching. AWS Config is also enabled in all regions and accounts provided.

The information from AWS Config and AWS Systems Manager Inventory is collected in S3 buckets in the deployment account and Athena Tables and Views are created to analyse the data using Amazon QuickSight. An AWS Lambda function [repairs](https://docs.aws.amazon.com/athena/latest/ug/msck-repair-table.html) the tables and creates an Athena datasource and two datasets for use in QuickSight, joining multiple tables for further insight. An additional AWS Lambda function is created to partition data from AWS Config.

## High Level Architecture

![Architecture Diagram](https://github.com/aelivingstone/patch-compliance/blob/master/images/Diagram.png)

## Motivation

Simplify installation, configuration and analysis of patch compliance information using data from AWS Config and AWS Systems Manager. Using data from AWS Config also allows for the analysis of unmanaged instances or instances that have been stopped or terminated. 

## Resources Created

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

## Prerequisites
All instances must be managed.

## License Summary
This reference code is made available under the MIT-0 license. See the LICENSE file.
