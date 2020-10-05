import time
import boto3
import logging

ACCOUNT_ID = None # Determined at runtime
REGION = None
DATABASE = 'patch_compliance'
AWS_APPLICATION_TABLE = 'aws_application'
AWS_AWS_COMPONENT_TABLE = 'aws_aws_component'
AWS_COMPLIANCE_ITEM_TABLE = 'aws_compliance_item'
AWS_CONFIG_SNAPSHOT_TABLE = 'aws_config_snapshot'
AWS_INSTANCE_DETAILED_INFORMATION_TABLE = 'aws_instance_detailed_information'
AWS_INSTANCE_INFORMATION_TABLE = 'aws_instance_information'
AWS_NETWORK_TABLE = 'aws_network'
AWS_PATCH_SUMMARY_TABLE = 'aws_patch_summary'
AWS_RESOURCE_GROUP_TABLE = 'aws_resource_group'
AWS_SERVICE_TABLE = 'aws_service'
AWS_TAG_TABLE = 'aws_tag'
AWS_WINDOWS_ROLE_TABLE = 'aws_windows_role'
AWS_WINDOWS_UPDATE_TABLE = 'aws_windows_update'
CONFIGMIC_TABLE = 'configmic'
CONFIGPC_TABLE = 'configpc'
PATCH_TABLE = 'patch'

client = boto3.client('quicksight')
athena = boto3.client('athena')
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    global ACCOUNT_ID
    global REGION
    global DATABASE
    global AWS_APPLICATION_TABLE
    global AWS_AWS_COMPONENT_TABLE
    global AWS_COMPLIANCE_ITEM_TABLE
    global AWS_CONFIG_SNAPSHOT_TABLE
    global AWS_INSTANCE_DETAILED_INFORMATION_TABLE
    global AWS_INSTANCE_INFORMATION_TABLE
    global AWS_NETWORK_TABLE
    global AWS_PATCH_SUMMARY_TABLE
    global AWS_RESOURCE_GROUP_TABLE
    global AWS_SERVICE_TABLE
    global AWS_TAG_TABLE
    global AWS_WINDOWS_ROLE_TABLE
    global AWS_WINDOWS_UPDATE_TABLE
    global CONFIGMIC_TABLE
    global CONFIGPC_TABLE
    global PATCH_TABLE    
    ACCOUNT_ID = context.invoked_function_arn.split(':')[4]
    REGION = context.invoked_function_arn.split(':')[3]

    # Need to run MSCK REPAIR TABLE on all tables https://docs.aws.amazon.com/athena/latest/ug/msck-repair-table.html
    response = athena.start_query_execution(
        QueryExecutionContext={'Database': DATABASE,},        
        QueryString='MSCK REPAIR TABLE ' +DATABASE + '.' +AWS_APPLICATION_TABLE,
        ResultConfiguration={'OutputLocation': 's3://aws-athena-query-results-180304385487-eu-west-1',}
    )
    logger.info ('MSCK REPAIR AWS_APPLICATION_TABLE: %s', response)
    response = athena.start_query_execution(
        QueryExecutionContext={'Database': DATABASE,},        
        QueryString='MSCK REPAIR TABLE ' +DATABASE + '.' +AWS_AWS_COMPONENT_TABLE,
        ResultConfiguration={'OutputLocation': 's3://aws-athena-query-results-180304385487-eu-west-1',}
    )
    logger.info ('MSCK REPAIR AWS_AWS_COMPONENT_TABLE: %s', response)
    response = athena.start_query_execution(
        QueryExecutionContext={'Database': DATABASE,},        
        QueryString='MSCK REPAIR TABLE ' +DATABASE + '.' +AWS_COMPLIANCE_ITEM_TABLE,
        ResultConfiguration={'OutputLocation': 's3://aws-athena-query-results-180304385487-eu-west-1',}
    )
    logger.info ('MSCK REPAIR AWS_COMPLIANCE_ITEM_TABLE: %s', response)
    response = athena.start_query_execution(
        QueryExecutionContext={'Database': DATABASE,},        
        QueryString='MSCK REPAIR TABLE ' +DATABASE + '.' +AWS_CONFIG_SNAPSHOT_TABLE,
        ResultConfiguration={'OutputLocation': 's3://aws-athena-query-results-180304385487-eu-west-1',}
    )
    logger.info ('MSCK REPAIR AWS_CONFIG_SNAPSHOT_TABLE: %s', response)
    response = athena.start_query_execution(
        QueryExecutionContext={'Database': DATABASE,},        
        QueryString='MSCK REPAIR TABLE ' +DATABASE + '.' +AWS_INSTANCE_DETAILED_INFORMATION_TABLE,
        ResultConfiguration={'OutputLocation': 's3://aws-athena-query-results-180304385487-eu-west-1',}
    )
    logger.info ('MSCK REPAIR AWS_INSTANCE_DETAILED_INFORMATION_TABLE: %s', response)
    response = athena.start_query_execution(
        QueryExecutionContext={'Database': DATABASE,},        
        QueryString='MSCK REPAIR TABLE ' +DATABASE + '.' +AWS_INSTANCE_INFORMATION_TABLE,
        ResultConfiguration={'OutputLocation': 's3://aws-athena-query-results-180304385487-eu-west-1',}
    )
    logger.info ('MSCK REPAIR AWS_INSTANCE_INFORMATION_TABLE: %s', response)
    response = athena.start_query_execution(
        QueryExecutionContext={'Database': DATABASE,},        
        QueryString='MSCK REPAIR TABLE ' +DATABASE + '.' +AWS_NETWORK_TABLE,
        ResultConfiguration={'OutputLocation': 's3://aws-athena-query-results-180304385487-eu-west-1',}
    )
    logger.info ('MSCK REPAIR AWS_NETWORK_TABLE: %s', response)
    response = athena.start_query_execution(
        QueryExecutionContext={'Database': DATABASE,},        
        QueryString='MSCK REPAIR TABLE ' +DATABASE + '.' +AWS_PATCH_SUMMARY_TABLE,
        ResultConfiguration={'OutputLocation': 's3://aws-athena-query-results-180304385487-eu-west-1',}
    )
    logger.info ('MSCK REPAIR AWS_PATCH_SUMMARY_TABLE: %s', response)
    response = athena.start_query_execution(
        QueryExecutionContext={'Database': DATABASE,},        
        QueryString='MSCK REPAIR TABLE ' +DATABASE + '.' +AWS_RESOURCE_GROUP_TABLE,
        ResultConfiguration={'OutputLocation': 's3://aws-athena-query-results-180304385487-eu-west-1',}
    )
    logger.info ('MSCK REPAIR AWS_RESOURCE_GROUP_TABLE: %s', response)
    response = athena.start_query_execution(
        QueryExecutionContext={'Database': DATABASE,},        
        QueryString='MSCK REPAIR TABLE ' +DATABASE + '.' +AWS_SERVICE_TABLE,
        ResultConfiguration={'OutputLocation': 's3://aws-athena-query-results-180304385487-eu-west-1',}
    )
    logger.info ('MSCK REPAIR AWS_SERVICE_TABLE: %s', response)
    response = athena.start_query_execution(
        QueryExecutionContext={'Database': DATABASE,},        
        QueryString='MSCK REPAIR TABLE ' +DATABASE + '.' +AWS_TAG_TABLE,
        ResultConfiguration={'OutputLocation': 's3://aws-athena-query-results-180304385487-eu-west-1',}
    )
    logger.info ('MSCK REPAIR AWS_TAG_TABLE: %s', response)
    response = athena.start_query_execution(
        QueryExecutionContext={'Database': DATABASE,},        
        QueryString='MSCK REPAIR TABLE ' +DATABASE + '.' +AWS_WINDOWS_ROLE_TABLE,
        ResultConfiguration={'OutputLocation': 's3://aws-athena-query-results-180304385487-eu-west-1',}
    )
    logger.info ('MSCK REPAIR AWS_WINDOWS_ROLE_TABLE: %s', response)
    response = athena.start_query_execution(
        QueryExecutionContext={'Database': DATABASE,},        
        QueryString='MSCK REPAIR TABLE ' +DATABASE + '.' +AWS_WINDOWS_UPDATE_TABLE,
        ResultConfiguration={'OutputLocation': 's3://aws-athena-query-results-180304385487-eu-west-1',}
    )
    logger.info ('MSCK REPAIR AWS_WINDOWS_UPDATE_TABLE: %s', response)

    # Managed Instance Compliance Check View
    response = athena.start_query_execution(
        QueryExecutionContext={
            'Database': DATABASE,
        },        
        QueryString="""
            CREATE OR REPLACE VIEW configmic AS 
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
            GROUP BY split(configurationItem.resourceid,'/')[2]""",
        ResultConfiguration={
            'OutputLocation': 's3://aws-athena-query-results-180304385487-eu-west-1',
        }
    )
    logger.info ('Create configmic view: %s', response)

    # Patch Compliance Check View
    response = athena.start_query_execution(
        QueryExecutionContext={
            'Database': DATABASE,
        },        
        QueryString="""
            CREATE OR REPLACE VIEW ConfigPC AS
            SELECT MAX(dt) as ConfigPCDate,
            split(configurationItem.resourceid,'/')[3] as ConfigPCInstanceID,
            MAX(json_extract_scalar(regexp_extract(configurationItem.configuration, '\\{[^}{.]*ec2-managedinstance-patch-compliance-status-check[^}.]*\\}'), '$.compliancetype')) as ConfigPCStatus
            FROM patch_compliance.aws_config_snapshot
            CROSS JOIN UNNEST(configurationitems) AS t1(configurationItem)
            WHERE regexp_like(configurationItem.configuration, '\\{[^}{.]*ec2-managedinstance-patch-compliance-status-check[^}.]*\\}')
            AND configurationItem.resourcetype = 'AWS::Config::ResourceCompliance'
            GROUP BY split(configurationItem.resourceid,'/')[3]
            ORDER BY MAX(dt) DESC""",
        ResultConfiguration={
            'OutputLocation': 's3://aws-athena-query-results-180304385487-eu-west-1',
        }
    )
    logger.info ('Create configpc view: %s', response)

    # Individual Patches View
    response = athena.start_query_execution(
        QueryExecutionContext={
            'Database': DATABASE,
        },        
        QueryString="""
            CREATE OR REPLACE VIEW Patch AS
            SELECT Status AS PatchStatus,
            InstalledTime AS PatchInstalledTime,
            ExecutionType AS PatchExecutionType,
            PatchSeverity AS PatchPatchSeverity,
            Title AS PatchTitle,
            Severity AS PatchSeverity,
            ExecutionTime AS PatchExecutionTime,
            ComplianceType AS PatchComplianceType,
            Classification AS PatchClassification,
            DocumentVersion AS PatchDocumentVersion,
            Id AS PatchId,
            PatchState AS PatchPatchState,
            PatchBaselineId AS PatchPatchBaselineId,
            DocumentName AS PatchDocumentName,
            PatchGroup AS PatchPatchGroup,
            ExecutionId AS PatchExecutionId,
            resourceId AS PatchresourceId,
            captureTime AS PatchcaptureTime,
            schemaVersion AS PatchschemaVersion
            FROM "patch_compliance"."aws_compliance_item"
            WHERE compliancetype = 'Patch'""",
        ResultConfiguration={
            'OutputLocation': 's3://aws-athena-query-results-180304385487-eu-west-1',
        }
    )
    logger.info ('Create patch view: %s', response)        
    
    response = client.delete_data_source(
        AwsAccountId=ACCOUNT_ID,
        DataSourceId='patchCompliance'
    )
    logger.info ('Delete Data Source: %s', response)

    # Create QuickSight Data Source
    response = client.create_data_source(
        AwsAccountId=ACCOUNT_ID,
        DataSourceId='patchCompliance',
        Name='Patch Compliance Data Source',
        Type='ATHENA',
        DataSourceParameters={
            'AthenaParameters': {
                'WorkGroup': 'primary'
            }
        },
        Permissions=[
            {
                'Principal': 'arn:aws:quicksight:' +REGION + ':' +ACCOUNT_ID + ':user/default/Admin/aliving-Isengard',
                'Actions': [
                    'quicksight:DescribeDataSource',
                    'quicksight:DescribeDataSourcePermissions',
                    'quicksight:PassDataSource',
                    'quicksight:UpdateDataSource',
                    'quicksight:DeleteDataSource',
                    'quicksight:UpdateDataSourcePermissions'                   
                ]
            },
        ]              
    )
    logger.info ('Create Data Source: %s', response)
    logger.info ('Data Source ARN: ' +response['Arn'])
    dataARN = response['Arn']

    response = client.delete_data_set(
        AwsAccountId=ACCOUNT_ID,
        DataSetId='patchComplianceDataSet'
    )
    logger.info ('Delete Data Source: %s', response)   
    time.sleep(1)     

    # Create QuickSight Data Set
    response = client.create_data_set(
        AwsAccountId=ACCOUNT_ID,
        DataSetId='patchComplianceDataSet',
        Name='Patch Compliance Data Set',
        Permissions=[
            {
                'Principal': 'arn:aws:quicksight:' +REGION + ':' +ACCOUNT_ID + ':user/default/Admin/aliving-Isengard',
                'Actions': [
                    'quicksight:UpdateDataSetPermissions',
                    'quicksight:DescribeDataSet',
                    'quicksight:DescribeDataSetPermissions',
                    'quicksight:PassDataSet',
                    'quicksight:DescribeIngestion',
                    'quicksight:ListIngestions',
                    'quicksight:UpdateDataSet',
                    'quicksight:DeleteDataSet',
                    'quicksight:CreateIngestion',
                    'quicksight:CancelIngestion'
                ]
            },
        ],           
        PhysicalTableMap={
            "awswindowsupdatephysicaltable": {
                "RelationalTable": {
                    "DataSourceArn": dataARN,
                    "Schema": "patch_compliance",
                    "Name": AWS_WINDOWS_UPDATE_TABLE,
                    "InputColumns": [
                        {
                            "Name": "accountid",
                            "Type": "STRING"
                        },
                        {
                            "Name": "resourceid",
                            "Type": "STRING"
                        },
                        {
                            "Name": "installedtime",
                            "Type": "STRING"
                        },
                        {
                            "Name": "description",
                            "Type": "STRING"
                        },
                        {
                            "Name": "installedby",
                            "Type": "STRING"
                        },
                        {
                            "Name": "region",
                            "Type": "STRING"
                        },
                        {
                            "Name": "hotfixid",
                            "Type": "STRING"
                        },
                        {
                            "Name": "resourcetype",
                            "Type": "STRING"
                        }
                    ]
                }
            },
            "awsresourcegroupphysicaltable": {
                "RelationalTable": {
                    "DataSourceArn": dataARN,
                    "Schema": "patch_compliance",
                    "Name": AWS_RESOURCE_GROUP_TABLE,
                    "InputColumns": [
                        {
                            "Name": "resourceid",
                            "Type": "STRING"
                        },
                        {
                            "Name": "cpusockets",
                            "Type": "STRING"
                        },
                        {
                            "Name": "cpus",
                            "Type": "STRING"
                        },
                        {
                            "Name": "cpuhyperthreadenabled",
                            "Type": "STRING"
                        },
                        {
                            "Name": "cpumodel",
                            "Type": "STRING"
                        },
                        {
                            "Name": "schemaversion",
                            "Type": "STRING"
                        },
                        {
                            "Name": "resourcetype",
                            "Type": "STRING"
                        },
                        {
                            "Name": "cpucores",
                            "Type": "STRING"
                        },
                        {
                            "Name": "accountid",
                            "Type": "STRING"
                        },
                        {
                            "Name": "osservicepack",
                            "Type": "STRING"
                        },
                        {
                            "Name": "cpuspeedmhz",
                            "Type": "STRING"
                        },
                        {
                            "Name": "capturetime",
                            "Type": "STRING"
                        },
                        {
                            "Name": "region",
                            "Type": "STRING"
                        }
                    ]
                }
            },
            "awscomplianceitemphysicaltable": {
                "RelationalTable": {
                    "DataSourceArn": dataARN,
                    "Schema": "patch_compliance",
                    "Name": AWS_COMPLIANCE_ITEM_TABLE,
                    "InputColumns": [
                        {
                            "Name": "severity",
                            "Type": "STRING"
                        },
                        {
                            "Name": "executiontime",
                            "Type": "STRING"
                        },
                        {
                            "Name": "resourceid",
                            "Type": "STRING"
                        },
                        {
                            "Name": "documentversion",
                            "Type": "STRING"
                        },
                        {
                            "Name": "patchstate",
                            "Type": "STRING"
                        },
                        {
                            "Name": "title",
                            "Type": "STRING"
                        },
                        {
                            "Name": "classification",
                            "Type": "STRING"
                        },
                        {
                            "Name": "schemaversion",
                            "Type": "STRING"
                        },
                        {
                            "Name": "resourcetype",
                            "Type": "STRING"
                        },
                        {
                            "Name": "patchgroup",
                            "Type": "STRING"
                        },
                        {
                            "Name": "patchseverity",
                            "Type": "STRING"
                        },
                        {
                            "Name": "executionid",
                            "Type": "STRING"
                        },
                        {
                            "Name": "accountid",
                            "Type": "STRING"
                        },
                        {
                            "Name": "installedtime",
                            "Type": "STRING"
                        },
                        {
                            "Name": "executiontype",
                            "Type": "STRING"
                        },
                        {
                            "Name": "capturetime",
                            "Type": "STRING"
                        },
                        {
                            "Name": "patchbaselineid",
                            "Type": "STRING"
                        },
                        {
                            "Name": "documentname",
                            "Type": "STRING"
                        },
                        {
                            "Name": "id",
                            "Type": "STRING"
                        },
                        {
                            "Name": "region",
                            "Type": "STRING"
                        },
                        {
                            "Name": "compliancetype",
                            "Type": "STRING"
                        },
                        {
                            "Name": "status",
                            "Type": "STRING"
                        }
                    ]
                }
            },
            "awsinstancedetailedinformationphysicaltable": {
                "RelationalTable": {
                    "DataSourceArn": dataARN,
                    "Schema": "patch_compliance",
                    "Name": AWS_INSTANCE_DETAILED_INFORMATION_TABLE,
                    "InputColumns": [
                        {
                            "Name": "resourceid",
                            "Type": "STRING"
                        },
                        {
                            "Name": "cpusockets",
                            "Type": "STRING"
                        },
                        {
                            "Name": "cpus",
                            "Type": "STRING"
                        },
                        {
                            "Name": "cpuhyperthreadenabled",
                            "Type": "STRING"
                        },
                        {
                            "Name": "cpumodel",
                            "Type": "STRING"
                        },
                        {
                            "Name": "schemaversion",
                            "Type": "STRING"
                        },
                        {
                            "Name": "resourcetype",
                            "Type": "STRING"
                        },
                        {
                            "Name": "cpucores",
                            "Type": "STRING"
                        },
                        {
                            "Name": "accountid",
                            "Type": "STRING"
                        },
                        {
                            "Name": "osservicepack",
                            "Type": "STRING"
                        },
                        {
                            "Name": "cpuspeedmhz",
                            "Type": "STRING"
                        },
                        {
                            "Name": "capturetime",
                            "Type": "STRING"
                        },
                        {
                            "Name": "region",
                            "Type": "STRING"
                        }
                    ]
                }
            },
            "configpcphysicaltable": {
                "RelationalTable": {
                    "DataSourceArn": dataARN,
                    "Schema": "patch_compliance",
                    "Name": CONFIGPC_TABLE,
                    "InputColumns": [
                        {
                            "Name": "configpcinstanceid",
                            "Type": "STRING"
                        },
                        {
                            "Name": "configpcstatus",
                            "Type": "STRING"
                        },
                        {
                            "Name": "configpcdate",
                            "Type": "STRING"
                        }
                    ]
                }
            },
            "awsapplicationphysicaltable": {
                "RelationalTable": {
                    "DataSourceArn": dataARN,
                    "Schema": "patch_compliance",
                    "Name": AWS_APPLICATION_TABLE,
                    "InputColumns": [
                        {
                            "Name": "summary",
                            "Type": "STRING"
                        },
                        {
                            "Name": "resourceid",
                            "Type": "STRING"
                        },
                        {
                            "Name": "release",
                            "Type": "STRING"
                        },
                        {
                            "Name": "packageid",
                            "Type": "STRING"
                        },
                        {
                            "Name": "schemaversion",
                            "Type": "STRING"
                        },
                        {
                            "Name": "version",
                            "Type": "STRING"
                        },
                        {
                            "Name": "resourcetype",
                            "Type": "STRING"
                        },
                        {
                            "Name": "url",
                            "Type": "STRING"
                        },
                        {
                            "Name": "accountid",
                            "Type": "STRING"
                        },
                        {
                            "Name": "installedtime",
                            "Type": "STRING"
                        },
                        {
                            "Name": "capturetime",
                            "Type": "STRING"
                        },
                        {
                            "Name": "name",
                            "Type": "STRING"
                        },
                        {
                            "Name": "publisher",
                            "Type": "STRING"
                        },
                        {
                            "Name": "region",
                            "Type": "STRING"
                        },
                        {
                            "Name": "applicationtype",
                            "Type": "STRING"
                        },
                        {
                            "Name": "architecture",
                            "Type": "STRING"
                        }
                    ]
                }
            },
            "awswindowsrolephysicaltable": {
                "RelationalTable": {
                    "DataSourceArn": dataARN,
                    "Schema": "patch_compliance",
                    "Name": AWS_WINDOWS_ROLE_TABLE,
                    "InputColumns": [
                        {
                            "Name": "parent",
                            "Type": "STRING"
                        },
                        {
                            "Name": "installed",
                            "Type": "STRING"
                        },
                        {
                            "Name": "resourceid",
                            "Type": "STRING"
                        },
                        {
                            "Name": "dependson",
                            "Type": "STRING"
                        },
                        {
                            "Name": "featuretype",
                            "Type": "STRING"
                        },
                        {
                            "Name": "description",
                            "Type": "STRING"
                        },
                        {
                            "Name": "schemaversion",
                            "Type": "STRING"
                        },
                        {
                            "Name": "resourcetype",
                            "Type": "STRING"
                        },
                        {
                            "Name": "path",
                            "Type": "STRING"
                        },
                        {
                            "Name": "subfeatures",
                            "Type": "STRING"
                        },
                        {
                            "Name": "accountid",
                            "Type": "STRING"
                        },
                        {
                            "Name": "servercomponentdescriptor",
                            "Type": "STRING"
                        },
                        {
                            "Name": "capturetime",
                            "Type": "STRING"
                        },
                        {
                            "Name": "displayname",
                            "Type": "STRING"
                        },
                        {
                            "Name": "name",
                            "Type": "STRING"
                        },
                        {
                            "Name": "region",
                            "Type": "STRING"
                        },
                        {
                            "Name": "installedstate",
                            "Type": "STRING"
                        }
                    ]
                }
            },
            "patchphysicaltable": {
                "RelationalTable": {
                    "DataSourceArn": dataARN,
                    "Schema": "patch_compliance",
                    "Name": PATCH_TABLE,
                    "InputColumns": [
                        {
                            "Name": "patchcompliancetype",
                            "Type": "STRING"
                        },
                        {
                            "Name": "patchpatchgroup",
                            "Type": "STRING"
                        },
                        {
                            "Name": "patchcapturetime",
                            "Type": "STRING"
                        },
                        {
                            "Name": "patchexecutionid",
                            "Type": "STRING"
                        },
                        {
                            "Name": "patchexecutiontype",
                            "Type": "STRING"
                        },
                        {
                            "Name": "patchpatchseverity",
                            "Type": "STRING"
                        },
                        {
                            "Name": "patchinstalledtime",
                            "Type": "STRING"
                        },
                        {
                            "Name": "patchclassification",
                            "Type": "STRING"
                        },
                        {
                            "Name": "patchdocumentversion",
                            "Type": "STRING"
                        },
                        {
                            "Name": "patchdocumentname",
                            "Type": "STRING"
                        },
                        {
                            "Name": "patchseverity",
                            "Type": "STRING"
                        },
                        {
                            "Name": "patchid",
                            "Type": "STRING"
                        },
                        {
                            "Name": "patchstatus",
                            "Type": "STRING"
                        },
                        {
                            "Name": "patchpatchstate",
                            "Type": "STRING"
                        },
                        {
                            "Name": "patchschemaversion",
                            "Type": "STRING"
                        },
                        {
                            "Name": "patchpatchbaselineid",
                            "Type": "STRING"
                        },
                        {
                            "Name": "patchtitle",
                            "Type": "STRING"
                        },
                        {
                            "Name": "patchresourceid",
                            "Type": "STRING"
                        },
                        {
                            "Name": "patchexecutiontime",
                            "Type": "STRING"
                        }
                    ]
                }
            },
            "awsnetworkphysicaltable": {
                "RelationalTable": {
                    "DataSourceArn": dataARN,
                    "Schema": "patch_compliance",
                    "Name": AWS_NETWORK_TABLE,
                    "InputColumns": [
                        {
                            "Name": "accountid",
                            "Type": "STRING"
                        },
                        {
                            "Name": "resourceid",
                            "Type": "STRING"
                        },
                        {
                            "Name": "ipv4",
                            "Type": "STRING"
                        },
                        {
                            "Name": "ipv6",
                            "Type": "STRING"
                        },
                        {
                            "Name": "dnsserver",
                            "Type": "STRING"
                        },
                        {
                            "Name": "name",
                            "Type": "STRING"
                        },
                        {
                            "Name": "dhcpserver",
                            "Type": "STRING"
                        },
                        {
                            "Name": "macaddress",
                            "Type": "STRING"
                        },
                        {
                            "Name": "region",
                            "Type": "STRING"
                        },
                        {
                            "Name": "subnetmask",
                            "Type": "STRING"
                        },
                        {
                            "Name": "resourcetype",
                            "Type": "STRING"
                        },
                        {
                            "Name": "gateway",
                            "Type": "STRING"
                        }
                    ]
                }
            },
            "awsinstanceinformationphysicaltable": {
                "RelationalTable": {
                    "DataSourceArn": dataARN,
                    "Schema": "patch_compliance",
                    "Name": AWS_INSTANCE_INFORMATION_TABLE,
                    "InputColumns": [
                        {
                            "Name": "agentversion",
                            "Type": "STRING"
                        },
                        {
                            "Name": "ipaddress",
                            "Type": "STRING"
                        },
                        {
                            "Name": "instancestatus",
                            "Type": "STRING"
                        },
                        {
                            "Name": "resourceid",
                            "Type": "STRING"
                        },
                        {
                            "Name": "computername",
                            "Type": "STRING"
                        },
                        {
                            "Name": "schemaversion",
                            "Type": "STRING"
                        },
                        {
                            "Name": "resourcetype",
                            "Type": "STRING"
                        },
                        {
                            "Name": "platformname",
                            "Type": "STRING"
                        },
                        {
                            "Name": "accountid",
                            "Type": "STRING"
                        },
                        {
                            "Name": "instanceid",
                            "Type": "STRING"
                        },
                        {
                            "Name": "agenttype",
                            "Type": "STRING"
                        },
                        {
                            "Name": "capturetime",
                            "Type": "STRING"
                        },
                        {
                            "Name": "platformtype",
                            "Type": "STRING"
                        },
                        {
                            "Name": "platformversion",
                            "Type": "STRING"
                        },
                        {
                            "Name": "region",
                            "Type": "STRING"
                        }
                    ]
                }
            },
            "awsservicephysicaltable": {
                "RelationalTable": {
                    "DataSourceArn": dataARN,
                    "Schema": "patch_compliance",
                    "Name": AWS_SERVICE_TABLE,
                    "InputColumns": [
                        {
                            "Name": "servicesdependedon",
                            "Type": "STRING"
                        },
                        {
                            "Name": "resourceid",
                            "Type": "STRING"
                        },
                        {
                            "Name": "dependentservices",
                            "Type": "STRING"
                        },
                        {
                            "Name": "schemaversion",
                            "Type": "STRING"
                        },
                        {
                            "Name": "resourcetype",
                            "Type": "STRING"
                        },
                        {
                            "Name": "accountid",
                            "Type": "STRING"
                        },
                        {
                            "Name": "servicetype",
                            "Type": "STRING"
                        },
                        {
                            "Name": "capturetime",
                            "Type": "STRING"
                        },
                        {
                            "Name": "displayname",
                            "Type": "STRING"
                        },
                        {
                            "Name": "starttype",
                            "Type": "STRING"
                        },
                        {
                            "Name": "name",
                            "Type": "STRING"
                        },
                        {
                            "Name": "region",
                            "Type": "STRING"
                        },
                        {
                            "Name": "status",
                            "Type": "STRING"
                        }
                    ]
                }
            },
            "configmicphysicaltable": {
                "RelationalTable": {
                    "DataSourceArn": dataARN,
                    "Schema": "patch_compliance",
                    "Name": CONFIGMIC_TABLE,
                    "InputColumns": [
                        {
                            "Name": "configmicinstanceid",
                            "Type": "STRING"
                        },
                        {
                            "Name": "configmicstate",
                            "Type": "STRING"
                        },
                        {
                            "Name": "configmicaccountid",
                            "Type": "STRING"
                        },
                        {
                            "Name": "configmicdate",
                            "Type": "STRING"
                        },
                        {
                            "Name": "configmicregion",
                            "Type": "STRING"
                        },
                        {
                            "Name": "configmiccompliancestatus",
                            "Type": "STRING"
                        },
                        {
                            "Name": "configmicname",
                            "Type": "STRING"
                        }
                    ]
                }
            },
            "awsawscomponentphysicaltable": {
                "RelationalTable": {
                    "DataSourceArn": dataARN,
                    "Schema": "patch_compliance",
                    "Name": AWS_AWS_COMPONENT_TABLE,
                    "InputColumns": [
                        {
                            "Name": "summary",
                            "Type": "STRING"
                        },
                        {
                            "Name": "resourceid",
                            "Type": "STRING"
                        },
                        {
                            "Name": "release",
                            "Type": "STRING"
                        },
                        {
                            "Name": "packageid",
                            "Type": "STRING"
                        },
                        {
                            "Name": "schemaversion",
                            "Type": "STRING"
                        },
                        {
                            "Name": "version",
                            "Type": "STRING"
                        },
                        {
                            "Name": "resourcetype",
                            "Type": "STRING"
                        },
                        {
                            "Name": "url",
                            "Type": "STRING"
                        },
                        {
                            "Name": "accountid",
                            "Type": "STRING"
                        },
                        {
                            "Name": "installedtime",
                            "Type": "STRING"
                        },
                        {
                            "Name": "capturetime",
                            "Type": "STRING"
                        },
                        {
                            "Name": "name",
                            "Type": "STRING"
                        },
                        {
                            "Name": "publisher",
                            "Type": "STRING"
                        },
                        {
                            "Name": "region",
                            "Type": "STRING"
                        },
                        {
                            "Name": "applicationtype",
                            "Type": "STRING"
                        },
                        {
                            "Name": "architecture",
                            "Type": "STRING"
                        }
                    ]
                }
            },
            "awstagphysicaltable": {
                "RelationalTable": {
                    "DataSourceArn": dataARN,
                    "Schema": "patch_compliance",
                    "Name": AWS_TAG_TABLE,
                    "InputColumns": [
                        {
                            "Name": "accountid",
                            "Type": "STRING"
                        },
                        {
                            "Name": "resourceid",
                            "Type": "STRING"
                        },
                        {
                            "Name": "capturetime",
                            "Type": "STRING"
                        },
                        {
                            "Name": "schemaversion",
                            "Type": "STRING"
                        },
                        {
                            "Name": "region",
                            "Type": "STRING"
                        },
                        {
                            "Name": "value",
                            "Type": "STRING"
                        },
                        {
                            "Name": "resourcetype",
                            "Type": "STRING"
                        },
                        {
                            "Name": "key",
                            "Type": "STRING"
                        }
                    ]
                }
            },
            "awspatchsummaryphysicaltable": {
                "RelationalTable": {
                    "DataSourceArn": dataARN,
                    "Schema": "patch_compliance",
                    "Name": AWS_PATCH_SUMMARY_TABLE,
                    "InputColumns": [
                        {
                            "Name": "installedothercount",
                            "Type": "STRING"
                        },
                        {
                            "Name": "resourceid",
                            "Type": "STRING"
                        },
                        {
                            "Name": "snapshotid",
                            "Type": "STRING"
                        },
                        {
                            "Name": "rebootoption",
                            "Type": "STRING"
                        },
                        {
                            "Name": "notapplicablecount",
                            "Type": "STRING"
                        },
                        {
                            "Name": "operationtype",
                            "Type": "STRING"
                        },
                        {
                            "Name": "schemaversion",
                            "Type": "STRING"
                        },
                        {
                            "Name": "resourcetype",
                            "Type": "STRING"
                        },
                        {
                            "Name": "baselineid",
                            "Type": "STRING"
                        },
                        {
                            "Name": "patchgroup",
                            "Type": "STRING"
                        },
                        {
                            "Name": "installedcount",
                            "Type": "STRING"
                        },
                        {
                            "Name": "accountid",
                            "Type": "STRING"
                        },
                        {
                            "Name": "installedpendingrebootcount",
                            "Type": "STRING"
                        },
                        {
                            "Name": "installedrejectedcount",
                            "Type": "STRING"
                        },
                        {
                            "Name": "missingcount",
                            "Type": "STRING"
                        },
                        {
                            "Name": "failedcount",
                            "Type": "STRING"
                        },
                        {
                            "Name": "capturetime",
                            "Type": "STRING"
                        },
                        {
                            "Name": "operationendtime",
                            "Type": "STRING"
                        },
                        {
                            "Name": "region",
                            "Type": "STRING"
                        },
                        {
                            "Name": "operationstarttime",
                            "Type": "STRING"
                        }
                    ]
                }
            }
        },

        LogicalTableMap={
            "awswindowsrolelogicaltable": {
                "Alias": "awswindowsrole",
                "DataTransforms": [
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "resourcetype",
                            "NewColumnName": "windowsroleresourcetype"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "region",
                            "NewColumnName": "windowsroleregion"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "accountid",
                            "NewColumnName": "windowsroleaccountid"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "schemaversion",
                            "NewColumnName": "windowsroleschemaversion"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "capturetime",
                            "NewColumnName": "windowsrolecapturetime"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "resourceid",
                            "NewColumnName": "windowsroleresourceid"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "servercomponentdescriptor",
                            "NewColumnName": "windowsroleservercomponentdescriptor"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "name",
                            "NewColumnName": "windowsrolename"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "installedstate",
                            "NewColumnName": "windowsroleinstalledstate"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "displayname",
                            "NewColumnName": "windowsroledisplayname"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "installed",
                            "NewColumnName": "windowsroleinstalled"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "parent",
                            "NewColumnName": "windowsroleparent"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "description",
                            "NewColumnName": "windowsroledescription"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "dependson",
                            "NewColumnName": "windowsroledependson"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "featuretype",
                            "NewColumnName": "windowsrolefeaturetype"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "path",
                            "NewColumnName": "windowsrolepath"
                        }
                    }
                ],
                "Source": {
                    "PhysicalTableId": "awswindowsrolephysicaltable"
                }
            },
            "patchsummaryjoinlogicaltable": {
                "Alias": "patchsummaryjoin",
                "Source": {
                    "JoinInstruction": {
                        "LeftOperand": "resourcegroupjoinlogicaltable",
                        "RightOperand": "patchsummarylogicaltable",
                        "Type": "LEFT",
                        "OnClause": "{configmicinstanceid} = {patchsummaryresourceid}"
                    }
                }
            },
            "tagjoinlogicaltable": {
                "Alias": "tagjoin",
                "Source": {
                    "JoinInstruction": {
                        "LeftOperand": "windowsrolejoinlogicaltable",
                        "RightOperand": "taglogicaltable",
                        "Type": "LEFT",
                        "OnClause": "{configmicinstanceid} = {tagresourceid}"
                    }
                }
            },
            "resourcegroupjoinlogicaltable": {
                "Alias": "resourcegroupjoin",
                "Source": {
                    "JoinInstruction": {
                        "LeftOperand": "servicejoinlogicaltable",
                        "RightOperand": "resourcegrouplogicaltable",
                        "Type": "LEFT",
                        "OnClause": "{configmicinstanceid} = {resourcegroupresourceid}"
                    }
                }
            },
            "windowsupdatelogicaltable": {
                "Alias": "awswindowsupdate",
                "DataTransforms": [
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "resourcetype",
                            "NewColumnName": "windowsupdateresourcetype"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "region",
                            "NewColumnName": "windowsupdateregion"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "accountid",
                            "NewColumnName": "windowsupdateaccountid"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "installedby",
                            "NewColumnName": "windowsupdateinstalledby"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "installedtime",
                            "NewColumnName": "windowsupdateinstalledtime"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "description",
                            "NewColumnName": "windowsupdatedescription"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "hotfixid",
                            "NewColumnName": "windowsupdatehotfixid"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "resourceid",
                            "NewColumnName": "windowsupdateresourceid"
                        }
                    }
                ],
                "Source": {
                    "PhysicalTableId": "awswindowsupdatephysicaltable"
                }
            },
            "awscomponentjoinlogicaltable": {
                "Alias": "awscomponentjoin",
                "Source": {
                    "JoinInstruction": {
                        "LeftOperand": "complianceitemjoinlogicaltable",
                        "RightOperand": "awscomponentlogicaltable",
                        "Type": "LEFT",
                        "OnClause": "{configmicinstanceid} = {awscomponentresourceid}"
                    }
                }
            },
            "patchsummarylogicaltable": {
                "Alias": "awspatchsummary",
                "DataTransforms": [
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "resourcetype",
                            "NewColumnName": "patchsummaryresourcetype"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "region",
                            "NewColumnName": "patchsummaryregion"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "accountid",
                            "NewColumnName": "patchsummaryaccountid"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "schemaversion",
                            "NewColumnName": "patchsummaryschemaversion"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "capturetime",
                            "NewColumnName": "patchsummarycapturetime"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "resourceid",
                            "NewColumnName": "patchsummaryresourceid"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "patchgroup",
                            "NewColumnName": "patchsummarypatchgroup"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "installedrejectedcount",
                            "NewColumnName": "patchsummaryinstalledrejectedcount"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "installedcount",
                            "NewColumnName": "patchsummaryinstalledcount"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "operationtype",
                            "NewColumnName": "patchsummaryoperationtype"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "failedcount",
                            "NewColumnName": "patchsummaryfailedcount"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "rebootoption",
                            "NewColumnName": "patchsummaryrebootoption"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "operationstarttime",
                            "NewColumnName": "patchsummaryoperationstarttime"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "notapplicablecount",
                            "NewColumnName": "patchsummarynotapplicablecount"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "snapshotid",
                            "NewColumnName": "patchsummarysnapshotid"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "installedpendingrebootcount",
                            "NewColumnName": "patchsummaryinstalledpendingrebootcount"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "operationendtime",
                            "NewColumnName": "patchsummaryoperationendtime"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "installedothercount",
                            "NewColumnName": "patchsummaryinstalledothercount"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "missingcount",
                            "NewColumnName": "patchsummarymissingcount"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "baselineid",
                            "NewColumnName": "patchsummarybaselineid"
                        }
                    },
                    {
                        "CastColumnTypeOperation": {
                            "ColumnName": "patchsummarymissingcount",
                            "NewColumnType": "INTEGER"
                        }
                    },
                    {
                        "CastColumnTypeOperation": {
                            "ColumnName": "patchsummaryinstalledothercount",
                            "NewColumnType": "INTEGER"
                        }
                    },
                    {
                        "CastColumnTypeOperation": {
                            "ColumnName": "patchsummarynotapplicablecount",
                            "NewColumnType": "INTEGER"
                        }
                    },
                    {
                        "CastColumnTypeOperation": {
                            "ColumnName": "patchsummaryfailedcount",
                            "NewColumnType": "INTEGER"
                        }
                    },
                    {
                        "CastColumnTypeOperation": {
                            "ColumnName": "patchsummaryinstalledcount",
                            "NewColumnType": "INTEGER"
                        }
                    },
                    {
                        "CastColumnTypeOperation": {
                            "ColumnName": "patchsummaryinstalledrejectedcount",
                            "NewColumnType": "INTEGER"
                        }
                    }
                ],
                "Source": {
                    "PhysicalTableId": "awspatchsummaryphysicaltable"
                }
            },
            "windowsupdatejoinlogicaltable": {
                "Alias": "windowsupdatejoin",
                "Source": {
                    "JoinInstruction": {
                        "LeftOperand": "configmiclogicaltable",
                        "RightOperand": "windowsupdatelogicaltable",
                        "Type": "LEFT",
                        "OnClause": "{configmicinstanceid} = {windowsupdateresourceid}"
                    }
                }
            },
            "servicelogicaltable": {
                "Alias": "awsservice",
                "DataTransforms": [
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "resourcetype",
                            "NewColumnName": "serviceresourcetype"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "region",
                            "NewColumnName": "serviceregion"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "accountid",
                            "NewColumnName": "serviceaccountid"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "schemaversion",
                            "NewColumnName": "serviceschemaversion"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "capturetime",
                            "NewColumnName": "servicecapturetime"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "resourceid",
                            "NewColumnName": "serviceresourceid"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "name",
                            "NewColumnName": "servicename"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "starttype",
                            "NewColumnName": "servicestarttype"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "dependentservices",
                            "NewColumnName": "servicedependentservices"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "displayname",
                            "NewColumnName": "servicedisplayname"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "servicesdependedon",
                            "NewColumnName": "serviceservicesdependedon"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "status",
                            "NewColumnName": "servicestatus"
                        }
                    }
                ],
                "Source": {
                    "PhysicalTableId": "awsservicephysicaltable"
                }
            },
            "networkjoinlogicaltable": {
                "Alias": "networkjoin",
                "Source": {
                    "JoinInstruction": {
                        "LeftOperand": "patchsummaryjoinlogicaltable",
                        "RightOperand": "networklogicaltable",
                        "Type": "LEFT",
                        "OnClause": "{configmicinstanceid} = {networkresourceid}"
                    }
                }
            },
            "complianceitemjoinlogicaltable": {
                "Alias": "complianceitemjoin",
                "Source": {
                    "JoinInstruction": {
                        "LeftOperand": "instancedetailedjoinlogicaltable",
                        "RightOperand": "complianceitemlogicaltable",
                        "Type": "LEFT",
                        "OnClause": "{configmicinstanceid} = {complianceitemresourceid}"
                    }
                }
            },
            "patchlogicaltable": {
                "Alias": "patch",
                "Source": {
                    "PhysicalTableId": "patchphysicaltable"
                }
            },
            "networklogicaltable": {
                "Alias": "awsnetwork",
                "DataTransforms": [
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "resourcetype",
                            "NewColumnName": "networkresourcetype"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "region",
                            "NewColumnName": "networkregion"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "accountid",
                            "NewColumnName": "networkaccountid"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "ipv6",
                            "NewColumnName": "networkipv6"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "ipv4",
                            "NewColumnName": "networkipv4"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "macaddress",
                            "NewColumnName": "networkmacaddress"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "dnsserver",
                            "NewColumnName": "networkdnsserver"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "dhcpserver",
                            "NewColumnName": "networkdhcpserver"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "gateway",
                            "NewColumnName": "networkgateway"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "subnetmask",
                            "NewColumnName": "networksubnetmask"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "name",
                            "NewColumnName": "networkname"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "resourceid",
                            "NewColumnName": "networkresourceid"
                        }
                    }
                ],
                "Source": {
                    "PhysicalTableId": "awsnetworkphysicaltable"
                }
            },
            "configpcjoinlogicaltable": {
                "Alias": "configpcjoin",
                "DataTransforms": [
                    {
                        "CreateColumnsOperation": {
                            "Columns": [
                                {
                                    "ColumnName": "windowsupdateinstalleddatetime",
                                    "ColumnId": "windowsupdateinstalleddatetime",
                                    "Expression": "parseDate(replace(substring({windowsupdateinstalledtime},1,19),'T',\" \"),'yyyy-MM-dd HH:mm:ss')"
                                }
                            ]
                        }
                    },
                    {
                        "CreateColumnsOperation": {
                            "Columns": [
                                {
                                    "ColumnName": "windowsrolecapturedatetime",
                                    "ColumnId": "windowsrolecapturedatetime",
                                    "Expression": "parseDate(replace(substring({windowsrolecapturetime},1,19),'T',\" \"),'yyyy-MM-dd HH:mm:ss')"
                                }
                            ]
                        }
                    },
                    {
                        "CreateColumnsOperation": {
                            "Columns": [
                                {
                                    "ColumnName": "tagcapturedatetime",
                                    "ColumnId": "tagcapturedatetime",
                                    "Expression": "parseDate(replace(substring({tagcapturetime},1,19),'T',\" \"),'yyyy-MM-dd HH:mm:ss')"
                                }
                            ]
                        }
                    },
                    {
                        "CreateColumnsOperation": {
                            "Columns": [
                                {
                                    "ColumnName": "servicecapturedatetime",
                                    "ColumnId": "servicecapturedatetime",
                                    "Expression": "parseDate(replace(substring({servicecapturetime},1,19),'T',\" \"),'yyyy-MM-dd HH:mm:ss')"
                                }
                            ]
                        }
                    },
                    {
                        "CreateColumnsOperation": {
                            "Columns": [
                                {
                                    "ColumnName": "resourcegroupcapturedatetime",
                                    "ColumnId": "resourcegroupcapturedatetime",
                                    "Expression": "parseDate(replace(substring({resourcegroupcapturetime},1,19),'T',\" \"),'yyyy-MM-dd HH:mm:ss')"
                                }
                            ]
                        }
                    },
                    {
                        "CreateColumnsOperation": {
                            "Columns": [
                                {
                                    "ColumnName": "patchsummaryoperationenddatetime",
                                    "ColumnId": "patchsummaryoperationenddatetime",
                                    "Expression": "parseDate(replace(substring({patchsummaryoperationendtime},1,19),'T',\" \"),'yyyy-MM-dd HH:mm:ss')"
                                }
                            ]
                        }
                    },
                    {
                        "CreateColumnsOperation": {
                            "Columns": [
                                {
                                    "ColumnName": "patchsummaryoperationstartdatetime",
                                    "ColumnId": "patchsummaryoperationstartdatetime",
                                    "Expression": "parseDate(replace(substring({patchsummaryoperationstarttime},1,19),'T',\" \"),'yyyy-MM-dd HH:mm:ss')"
                                }
                            ]
                        }
                    },
                    {
                        "CreateColumnsOperation": {
                            "Columns": [
                                {
                                    "ColumnName": "patchsummarycapturedatetime",
                                    "ColumnId": "patchsummarycapturedatetime",
                                    "Expression": "parseDate(replace(substring({patchsummarycapturetime},1,19),'T',\" \"),'yyyy-MM-dd HH:mm:ss')"
                                }
                            ]
                        }
                    },
                    {
                        "CreateColumnsOperation": {
                            "Columns": [
                                {
                                    "ColumnName": "instancedetailedcapturedatetime",
                                    "ColumnId": "instancedetailedcapturedatetime",
                                    "Expression": "parseDate(replace(substring({instancedetailedcapturetime},1,19),'T',\" \"),'yyyy-MM-dd HH:mm:ss')"
                                }
                            ]
                        }
                    },
                    {
                        "CreateColumnsOperation": {
                            "Columns": [
                                {
                                    "ColumnName": "complianceitemexecutiondatetime",
                                    "ColumnId": "complianceitemexecutiondatetime",
                                    "Expression": "parseDate(replace(substring({complianceitemexecutiontime},1,19),'T',\" \"),'yyyy-MM-dd HH:mm:ss')"
                                }
                            ]
                        }
                    },
                    {
                        "CreateColumnsOperation": {
                            "Columns": [
                                {
                                    "ColumnName": "complianceitemcapturedatetime",
                                    "ColumnId": "complianceitemcapturedatetime",
                                    "Expression": "parseDate(replace(substring({complianceitemcapturetime},1,19),'T',\" \"),'yyyy-MM-dd HH:mm:ss')"
                                }
                            ]
                        }
                    },
                    {
                        "CreateColumnsOperation": {
                            "Columns": [
                                {
                                    "ColumnName": "awscomponentinstalleddatetime",
                                    "ColumnId": "awscomponentinstalleddatetime",
                                    "Expression": "parseDate(replace(substring({awscomponentinstalledtime},1,19),'T',\" \"),'yyyy-MM-dd HH:mm:ss')"
                                }
                            ]
                        }
                    },
                    {
                        "CreateColumnsOperation": {
                            "Columns": [
                                {
                                    "ColumnName": "awscomponentcapturedatetime",
                                    "ColumnId": "awscomponentcapturedatetime",
                                    "Expression": "parseDate(replace(substring({awscomponentcapturetime},1,19),'T',\" \"),'yyyy-MM-dd HH:mm:ss')"
                                }
                            ]
                        }
                    },
                    {
                        "CreateColumnsOperation": {
                            "Columns": [
                                {
                                    "ColumnName": "applicationinstalleddatetime",
                                    "ColumnId": "applicationinstalleddatetime",
                                    "Expression": "parseDate(replace(substring({applicationinstalledtime},1,19),'T',\" \"),'yyyy-MM-dd HH:mm:ss')"
                                }
                            ]
                        }
                    },
                    {
                        "CreateColumnsOperation": {
                            "Columns": [
                                {
                                    "ColumnName": "applicationcapturedatetime",
                                    "ColumnId": "applicationcapturedatetime",
                                    "Expression": "parseDate(replace(substring({applicationcapturetime},1,19),'T',\" \"),'yyyy-MM-dd HH:mm:ss')"
                                }
                            ]
                        }
                    },
                    {
                        "CreateColumnsOperation": {
                            "Columns": [
                                {
                                    "ColumnName": "instanceinformationcapturedatetime",
                                    "ColumnId": "instanceinformationcapturedatetime",
                                    "Expression": "parseDate(replace(substring({instanceinformationcapturetime},1,19),'T',\" \"),'yyyy-MM-dd HH:mm:ss')"
                                }
                            ]
                        }
                    },
                    {
                        "CreateColumnsOperation": {
                            "Columns": [
                                {
                                    "ColumnName": "patchexecutiondatetime",
                                    "ColumnId": "patchexecutiondatetime",
                                    "Expression": "parseDate(replace(substring({patchexecutiontime},1,19),'T',\" \"),'yyyy-MM-dd HH:mm:ss')"
                                }
                            ]
                        }
                    },
                    {
                        "CreateColumnsOperation": {
                            "Columns": [
                                {
                                    "ColumnName": "patchcapturedatetime",
                                    "ColumnId": "patchcapturedatetime",
                                    "Expression": "parseDate(replace(substring({patchcapturetime},1,19),'T',\" \"),'yyyy-MM-dd HH:mm:ss')"
                                }
                            ]
                        }
                    },
                    {
                        "CreateColumnsOperation": {
                            "Columns": [
                                {
                                    "ColumnName": "patchinstalleddatetime",
                                    "ColumnId": "patchinstalleddatetime",
                                    "Expression": "ifelse(strlen({patchinstalledtime})>0,parseDate(replace(substring({patchinstalledtime},1,19),'T',\" \"),'yyyy-MM-dd HH:mm:ss'),NULL)"
                                }
                            ]
                        }
                    },
                    {
                        "CreateColumnsOperation": {
                            "Columns": [
                                {
                                    "ColumnName": "complianceiteminstalleddatetime",
                                    "ColumnId": "complianceiteminstalleddatetime",
                                    "Expression": "ifelse(strlen({complianceiteminstalledtime})>0,parseDate(replace(substring({complianceiteminstalledtime},1,19),'T',\" \"),'yyyy-MM-dd HH:mm:ss'),NULL)"
                                }
                            ]
                        }
                    },
                    {
                        "ProjectOperation": {
                            "ProjectedColumns": [
                                "configmicdate",
                                "configmicaccountid",
                                "configmicregion",
                                "configmicinstanceid",
                                "configmicname",
                                "configmicstate",
                                "configmiccompliancestatus",
                                "windowsupdateresourceid",
                                "windowsupdatehotfixid",
                                "windowsupdatedescription",
                                "windowsupdateinstalledby",
                                "windowsrolepath",
                                "windowsrolefeaturetype",
                                "windowsroledependson",
                                "windowsroledescription",
                                "windowsroleparent",
                                "windowsroleinstalled",
                                "windowsroledisplayname",
                                "windowsroleinstalledstate",
                                "subfeatures",
                                "windowsrolename",
                                "windowsroleservercomponentdescriptor",
                                "windowsroleresourceid",
                                "tagkey",
                                "tagvalue",
                                "tagresourceid",
                                "servicestatus",
                                "servicetype",
                                "serviceservicesdependedon",
                                "servicedisplayname",
                                "servicedependentservices",
                                "servicestarttype",
                                "servicename",
                                "serviceresourceid",
                                "resourcegroupcpus",
                                "resourcegrouposservicepack",
                                "resourcegroupcpuhyperthreadenabled",
                                "resourcegroupcpuspeedmhz",
                                "resourcegroupcpusockets",
                                "resourcegroupcpucores",
                                "resourcegroupcpumodel",
                                "resourcegroupresourceid",
                                "patchsummarybaselineid",
                                "patchsummarymissingcount",
                                "patchsummaryinstalledothercount",
                                "patchsummaryinstalledpendingrebootcount",
                                "patchsummarysnapshotid",
                                "patchsummarynotapplicablecount",
                                "patchsummaryrebootoption",
                                "patchsummaryfailedcount",
                                "patchsummaryoperationtype",
                                "patchsummaryinstalledcount",
                                "patchsummaryinstalledrejectedcount",
                                "patchsummarypatchgroup",
                                "patchsummaryresourceid",
                                "networkresourceid",
                                "networkname",
                                "networksubnetmask",
                                "networkgateway",
                                "networkdhcpserver",
                                "networkdnsserver",
                                "networkmacaddress",
                                "networkipv4",
                                "networkipv6",
                                "instancedetailedcpus",
                                "instancedetailedosservicepack",
                                "instancedetailedcpuhyperthreadenabled",
                                "instancedetailedcpuspeedmhz",
                                "instancedetailedcpusockets",
                                "instancedetailedcpucores",
                                "instancedetailedcpumodel",
                                "instancedetailedresourceid",
                                "complianceitemstatus",
                                "complianceitemexecutiontype",
                                "complianceitempatchseverity",
                                "complianceitemtitle",
                                "complianceitemseverity",
                                "complianceitemcompliancetype",
                                "complianceitemclassification",
                                "complianceitemdocumentversion",
                                "complianceitemid",
                                "complianceitempatchstate",
                                "complianceitempatchbaselineid",
                                "complianceitemdocumentname",
                                "complianceitempatchgroup",
                                "complianceitemexecutionid",
                                "complianceitemresourceid",
                                "awscomponentapplicationtype",
                                "awscomponentarchitecture",
                                "awscomponentversion",
                                "awscomponentsummary",
                                "awscomponentpackageid",
                                "awscomponentpublisher",
                                "awscomponentrelease",
                                "awscomponenturl",
                                "awscomponentname",
                                "awscomponentresourceid",
                                "applicationtype",
                                "applicationarchitecture",
                                "applicationversion",
                                "applicationsummary",
                                "applicationpackageid",
                                "applicationpublisher",
                                "applicationrelease",
                                "applicationurl",
                                "applicationname",
                                "applicationresourceid",
                                "instanceinformationplatformname",
                                "instanceinformationplatformversion",
                                "instanceinformationagenttype",
                                "instanceinformationagentversion",
                                "instanceinformationinstanceid",
                                "instanceinformationinstancestatus",
                                "instanceinformationcomputername",
                                "instanceinformationipaddress",
                                "instanceinformationplatformtype",
                                "instanceinformationresourceid",
                                "patchstatus",
                                "patchexecutiontype",
                                "patchpatchseverity",
                                "patchtitle",
                                "patchseverity",
                                "patchcompliancetype",
                                "patchclassification",
                                "patchdocumentversion",
                                "patchid",
                                "patchpatchstate",
                                "patchpatchbaselineid",
                                "patchdocumentname",
                                "patchpatchgroup",
                                "patchexecutionid",
                                "patchresourceid",
                                "configpcdate",
                                "configpcinstanceid",
                                "configpcstatus",
                                "windowsupdateinstalleddatetime",
                                "windowsrolecapturedatetime",
                                "tagcapturedatetime",
                                "servicecapturedatetime",
                                "resourcegroupcapturedatetime",
                                "patchsummaryoperationenddatetime",
                                "patchsummaryoperationstartdatetime",
                                "patchsummarycapturedatetime",
                                "instancedetailedcapturedatetime",
                                "complianceitemexecutiondatetime",
                                "complianceitemcapturedatetime",
                                "awscomponentinstalleddatetime",
                                "awscomponentcapturedatetime",
                                "applicationinstalleddatetime",
                                "applicationcapturedatetime",
                                "instanceinformationcapturedatetime",
                                "patchexecutiondatetime",
                                "patchcapturedatetime",
                                "patchinstalleddatetime",
                                "complianceiteminstalleddatetime"
                            ]
                        }
                    }
                ],
                "Source": {
                    "JoinInstruction": {
                        "LeftOperand": "patchjoinlogicaltable",
                        "RightOperand": "configpclogicaltable",
                        "Type": "LEFT",
                        "OnClause": "{configmicinstanceid} = {configpcinstanceid}"
                    }
                }
            },
            "instancedetailedjoinlogicaltable": {
                "Alias": "instancedetailedjoin",
                "Source": {
                    "JoinInstruction": {
                        "LeftOperand": "networkjoinlogicaltable",
                        "RightOperand": "instancedetailedinformationlogicaltable",
                        "Type": "LEFT",
                        "OnClause": "{configmicinstanceid} = {instancedetailedresourceid}"
                    }
                }
            },
            "windowsrolejoinlogicaltable": {
                "Alias": "windowsrolejoin",
                "Source": {
                    "JoinInstruction": {
                        "LeftOperand": "windowsupdatejoinlogicaltable",
                        "RightOperand": "awswindowsrolelogicaltable",
                        "Type": "LEFT",
                        "OnClause": "{configmicinstanceid} = {windowsroleresourceid}"
                    }
                }
            },
            "taglogicaltable": {
                "Alias": "awstag",
                "DataTransforms": [
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "resourcetype",
                            "NewColumnName": "tagresourcetype"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "region",
                            "NewColumnName": "tagregion"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "accountid",
                            "NewColumnName": "tagaccountid"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "schemaversion",
                            "NewColumnName": "tagschemaversion"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "capturetime",
                            "NewColumnName": "tagcapturetime"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "resourceid",
                            "NewColumnName": "tagresourceid"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "value",
                            "NewColumnName": "tagvalue"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "key",
                            "NewColumnName": "tagkey"
                        }
                    }
                ],
                "Source": {
                    "PhysicalTableId": "awstagphysicaltable"
                }
            },
            "configmiclogicaltable": {
                "Alias": "configmic",
                "DataTransforms": [
                    {
                        "CastColumnTypeOperation": {
                            "ColumnName": "configmicdate",
                            "NewColumnType": "DATETIME",
                            "Format": "yyyy-MM-dd"
                        }
                    }
                ],
                "Source": {
                    "PhysicalTableId": "configmicphysicaltable"
                }
            },
            "applicationresourcejoinlogicaltable": {
                "Alias": "applicationresourcejoin",
                "Source": {
                    "JoinInstruction": {
                        "LeftOperand": "awscomponentjoinlogicaltable",
                        "RightOperand": "applicationlogicaltable",
                        "Type": "LEFT",
                        "OnClause": "{configmicinstanceid} = {applicationresourceid}"
                    }
                }
            },
            "configpclogicaltable": {
                "Alias": "configpc",
                "Source": {
                    "PhysicalTableId": "configpcphysicaltable"
                }
            },
            "instancedetailedinformationlogicaltable": {
                "Alias": "awsinstancedetailedinformation",
                "DataTransforms": [
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "resourcetype",
                            "NewColumnName": "instancedetailedresourcetype"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "region",
                            "NewColumnName": "instancedetailedregion"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "accountid",
                            "NewColumnName": "instancedetailedaccountid"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "schemaversion",
                            "NewColumnName": "instancedetailedschemaversion"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "capturetime",
                            "NewColumnName": "instancedetailedcapturetime"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "resourceid",
                            "NewColumnName": "instancedetailedresourceid"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "cpumodel",
                            "NewColumnName": "instancedetailedcpumodel"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "cpucores",
                            "NewColumnName": "instancedetailedcpucores"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "cpusockets",
                            "NewColumnName": "instancedetailedcpusockets"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "cpuspeedmhz",
                            "NewColumnName": "instancedetailedcpuspeedmhz"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "cpuhyperthreadenabled",
                            "NewColumnName": "instancedetailedcpuhyperthreadenabled"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "osservicepack",
                            "NewColumnName": "instancedetailedosservicepack"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "cpus",
                            "NewColumnName": "instancedetailedcpus"
                        }
                    },
                    {
                        "CastColumnTypeOperation": {
                            "ColumnName": "instancedetailedcpus",
                            "NewColumnType": "INTEGER"
                        }
                    },
                    {
                        "CastColumnTypeOperation": {
                            "ColumnName": "instancedetailedcpusockets",
                            "NewColumnType": "INTEGER"
                        }
                    },
                    {
                        "CastColumnTypeOperation": {
                            "ColumnName": "instancedetailedcpucores",
                            "NewColumnType": "INTEGER"
                        }
                    }
                ],
                "Source": {
                    "PhysicalTableId": "awsinstancedetailedinformationphysicaltable"
                }
            },
            "instanceinformationjoinlogicaltable": {
                "Alias": "instanceinformationjoin",
                "Source": {
                    "JoinInstruction": {
                        "LeftOperand": "applicationresourcejoinlogicaltable",
                        "RightOperand": "instanceinformationlogicaltable",
                        "Type": "LEFT",
                        "OnClause": "{configmicinstanceid} = {instanceinformationinstanceid}"
                    }
                }
            },
            "servicejoinlogicaltable": {
                "Alias": "servicejoin",
                "Source": {
                    "JoinInstruction": {
                        "LeftOperand": "tagjoinlogicaltable",
                        "RightOperand": "servicelogicaltable",
                        "Type": "LEFT",
                        "OnClause": "{configmicinstanceid} = {serviceresourceid}"
                    }
                }
            },
            "complianceitemlogicaltable": {
                "Alias": "awscomplianceitem",
                "DataTransforms": [
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "resourcetype",
                            "NewColumnName": "complianceitemresourcetype"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "region",
                            "NewColumnName": "complianceitemregion"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "accountid",
                            "NewColumnName": "complianceitemaccountid"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "schemaversion",
                            "NewColumnName": "complianceitemschemaversion"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "capturetime",
                            "NewColumnName": "complianceitemcapturetime"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "resourceid",
                            "NewColumnName": "complianceitemresourceid"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "executionid",
                            "NewColumnName": "complianceitemexecutionid"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "patchgroup",
                            "NewColumnName": "complianceitempatchgroup"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "documentname",
                            "NewColumnName": "complianceitemdocumentname"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "patchbaselineid",
                            "NewColumnName": "complianceitempatchbaselineid"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "patchstate",
                            "NewColumnName": "complianceitempatchstate"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "id",
                            "NewColumnName": "complianceitemid"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "documentversion",
                            "NewColumnName": "complianceitemdocumentversion"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "classification",
                            "NewColumnName": "complianceitemclassification"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "compliancetype",
                            "NewColumnName": "complianceitemcompliancetype"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "executiontime",
                            "NewColumnName": "complianceitemexecutiontime"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "severity",
                            "NewColumnName": "complianceitemseverity"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "title",
                            "NewColumnName": "complianceitemtitle"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "patchseverity",
                            "NewColumnName": "complianceitempatchseverity"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "executiontype",
                            "NewColumnName": "complianceitemexecutiontype"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "installedtime",
                            "NewColumnName": "complianceiteminstalledtime"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "status",
                            "NewColumnName": "complianceitemstatus"
                        }
                    }
                ],
                "Source": {
                    "PhysicalTableId": "awscomplianceitemphysicaltable"
                }
            },
            "patchjoinlogicaltable": {
                "Alias": "patchjoin",
                "Source": {
                    "JoinInstruction": {
                        "LeftOperand": "instanceinformationjoinlogicaltable",
                        "RightOperand": "patchlogicaltable",
                        "Type": "LEFT",
                        "OnClause": "{configmicinstanceid} = {patchresourceid}"
                    }
                }
            },
            "awscomponentlogicaltable": {
                "Alias": "awsawscomponent",
                "DataTransforms": [
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "resourcetype",
                            "NewColumnName": "awscomponentresourcetype"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "region",
                            "NewColumnName": "awscomponentregion"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "accountid",
                            "NewColumnName": "awscomponentaccountid"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "schemaversion",
                            "NewColumnName": "awscomponentschemaversion"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "capturetime",
                            "NewColumnName": "awscomponentcapturetime"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "resourceid",
                            "NewColumnName": "awscomponentresourceid"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "name",
                            "NewColumnName": "awscomponentname"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "url",
                            "NewColumnName": "awscomponenturl"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "release",
                            "NewColumnName": "awscomponentrelease"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "publisher",
                            "NewColumnName": "awscomponentpublisher"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "packageid",
                            "NewColumnName": "awscomponentpackageid"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "summary",
                            "NewColumnName": "awscomponentsummary"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "version",
                            "NewColumnName": "awscomponentversion"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "architecture",
                            "NewColumnName": "awscomponentarchitecture"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "installedtime",
                            "NewColumnName": "awscomponentinstalledtime"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "applicationtype",
                            "NewColumnName": "awscomponentapplicationtype"
                        }
                    }
                ],
                "Source": {
                    "PhysicalTableId": "awsawscomponentphysicaltable"
                }
            },
            "applicationlogicaltable": {
                "Alias": "awsapplication",
                "DataTransforms": [
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "resourcetype",
                            "NewColumnName": "applicationresourcetype"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "region",
                            "NewColumnName": "applicationregion"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "accountid",
                            "NewColumnName": "applicationaccountid"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "schemaversion",
                            "NewColumnName": "applicationschemaversion"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "capturetime",
                            "NewColumnName": "applicationcapturetime"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "resourceid",
                            "NewColumnName": "applicationresourceid"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "name",
                            "NewColumnName": "applicationname"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "url",
                            "NewColumnName": "applicationurl"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "release",
                            "NewColumnName": "applicationrelease"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "publisher",
                            "NewColumnName": "applicationpublisher"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "packageid",
                            "NewColumnName": "applicationpackageid"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "summary",
                            "NewColumnName": "applicationsummary"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "version",
                            "NewColumnName": "applicationversion"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "architecture",
                            "NewColumnName": "applicationarchitecture"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "installedtime",
                            "NewColumnName": "applicationinstalledtime"
                        }
                    }
                ],
                "Source": {
                    "PhysicalTableId": "awsapplicationphysicaltable"
                }
            },
            "instanceinformationlogicaltable": {
                "Alias": "awsinstanceinformation",
                "DataTransforms": [
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "resourcetype",
                            "NewColumnName": "instanceinformationresourcetype"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "region",
                            "NewColumnName": "instanceinformationregion"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "accountid",
                            "NewColumnName": "instanceinformationaccountid"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "schemaversion",
                            "NewColumnName": "instanceinformationschemaversion"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "capturetime",
                            "NewColumnName": "instanceinformationcapturetime"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "resourceid",
                            "NewColumnName": "instanceinformationresourceid"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "platformtype",
                            "NewColumnName": "instanceinformationplatformtype"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "ipaddress",
                            "NewColumnName": "instanceinformationipaddress"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "computername",
                            "NewColumnName": "instanceinformationcomputername"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "instancestatus",
                            "NewColumnName": "instanceinformationinstancestatus"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "instanceid",
                            "NewColumnName": "instanceinformationinstanceid"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "agentversion",
                            "NewColumnName": "instanceinformationagentversion"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "agenttype",
                            "NewColumnName": "instanceinformationagenttype"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "platformversion",
                            "NewColumnName": "instanceinformationplatformversion"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "platformname",
                            "NewColumnName": "instanceinformationplatformname"
                        }
                    }
                ],
                "Source": {
                    "PhysicalTableId": "awsinstanceinformationphysicaltable"
                }
            },
            "resourcegrouplogicaltable": {
                "Alias": "awsresourcegroup",
                "DataTransforms": [
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "resourcetype",
                            "NewColumnName": "resourcegroupresourcetype"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "region",
                            "NewColumnName": "resourcegroupregion"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "accountid",
                            "NewColumnName": "resourcegroupaccountid"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "schemaversion",
                            "NewColumnName": "resourcegroupschemaversion"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "capturetime",
                            "NewColumnName": "resourcegroupcapturetime"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "resourceid",
                            "NewColumnName": "resourcegroupresourceid"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "cpumodel",
                            "NewColumnName": "resourcegroupcpumodel"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "cpucores",
                            "NewColumnName": "resourcegroupcpucores"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "cpusockets",
                            "NewColumnName": "resourcegroupcpusockets"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "cpuspeedmhz",
                            "NewColumnName": "resourcegroupcpuspeedmhz"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "cpuhyperthreadenabled",
                            "NewColumnName": "resourcegroupcpuhyperthreadenabled"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "osservicepack",
                            "NewColumnName": "resourcegrouposservicepack"
                        }
                    },
                    {
                        "RenameColumnOperation": {
                            "ColumnName": "cpus",
                            "NewColumnName": "resourcegroupcpus"
                        }
                    },
                    {
                        "CastColumnTypeOperation": {
                            "ColumnName": "resourcegroupcpus",
                            "NewColumnType": "INTEGER"
                        }
                    },
                    {
                        "CastColumnTypeOperation": {
                            "ColumnName": "resourcegroupcpusockets",
                            "NewColumnType": "INTEGER"
                        }
                    },
                    {
                        "CastColumnTypeOperation": {
                            "ColumnName": "resourcegroupcpucores",
                            "NewColumnType": "INTEGER"
                        }
                    }
                ],
                "Source": {
                    "PhysicalTableId": "awsresourcegroupphysicaltable"
                }
            }
        },
        ImportMode='SPICE',
    )
    logger.info ('Create Data Set: %s', response)