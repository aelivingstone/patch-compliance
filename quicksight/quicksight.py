import time
import boto3
import logging
import cfnresponse

ACCOUNT_ID = None # Determined at runtime
REGION = None # Determined at runtime
DATABASE = None # Determined at runtime
AWS_APPLICATION_TABLE = None # Determined at runtime
AWS_AWS_COMPONENT_TABLE = None # Determined at runtime
AWS_COMPLIANCE_ITEM_TABLE = None # Determined at runtime
AWS_CONFIG_SNAPSHOT_TABLE = None # Determined at runtime
AWS_INSTANCE_DETAILED_INFORMATION_TABLE = None # Determined at runtime
AWS_INSTANCE_INFORMATION_TABLE = None # Determined at runtime
AWS_NETWORK_TABLE = None # Determined at runtime
AWS_PATCH_SUMMARY_TABLE = None # Determined at runtime
AWS_RESOURCE_GROUP_TABLE = None # Determined at runtime
AWS_SERVICE_TABLE = None # Determined at runtime
AWS_TAG_TABLE = None # Determined at runtime
AWS_WINDOWS_ROLE_TABLE = None # Determined at runtime
AWS_WINDOWS_UPDATE_TABLE = None # Determined at runtime
ATHENA_S3_BUCKET = None # Determined at runtime
CONFIGMIC_TABLE = None # Determined at runtime
CONFIGPC_TABLE = None # Determined at runtime
PATCH_TABLE = None # Determined at runtime
QUICKSIGHT_USER = None # Determined at runtime

client = boto3.client('quicksight')
athena = boto3.client('athena')
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def quicksight_handler(event, context):
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
    global ATHENA_S3_BUCKET
    global QUICKSIGHT_USER

    ACCOUNT_ID = context.invoked_function_arn.split(':')[4]
    REGION = context.invoked_function_arn.split(':')[3]
    DATABASE = event['ResourceProperties']['Database']
    AWS_APPLICATION_TABLE = event['ResourceProperties']['ApplicationTable']
    AWS_AWS_COMPONENT_TABLE = event['ResourceProperties']['ComponentTable']
    AWS_COMPLIANCE_ITEM_TABLE = event['ResourceProperties']['ComplianceItemTable']
    AWS_CONFIG_SNAPSHOT_TABLE = event['ResourceProperties']['ConfigSnapshotTable']
    AWS_INSTANCE_DETAILED_INFORMATION_TABLE = event['ResourceProperties']['InstanceDetailedInformationTable']
    AWS_INSTANCE_INFORMATION_TABLE = event['ResourceProperties']['InstanceInformationTable']
    AWS_NETWORK_TABLE = event['ResourceProperties']['NetworkTable']
    AWS_PATCH_SUMMARY_TABLE = event['ResourceProperties']['PatchSummaryTable']
    AWS_RESOURCE_GROUP_TABLE = event['ResourceProperties']['ResourceGroupTable']
    AWS_SERVICE_TABLE = event['ResourceProperties']['ServiceTable']
    AWS_TAG_TABLE = event['ResourceProperties']['TagTable']
    AWS_WINDOWS_ROLE_TABLE = event['ResourceProperties']['WindowsRoleTable']
    AWS_WINDOWS_UPDATE_TABLE = event['ResourceProperties']['WindowsUpdateTable']
    ATHENA_S3_BUCKET = 's3://' +event['ResourceProperties']['AthenaS3Bucket']
    CONFIGMIC_TABLE = event['ResourceProperties']['ConfgigMICTable']
    CONFIGPC_TABLE = event['ResourceProperties']['ConfigPCTable']
    PATCH_TABLE = event['ResourceProperties']['PatchTable']  
    QUICKSIGHT_USER = event['ResourceProperties']['QuickSightUser']   

    # Need to run MSCK REPAIR TABLE on all tables https://docs.aws.amazon.com/athena/latest/ug/msck-repair-table.html
    response = athena.start_query_execution(
        QueryExecutionContext={'Database': DATABASE,},        
        QueryString='MSCK REPAIR TABLE ' +DATABASE + '.' +AWS_APPLICATION_TABLE,
        ResultConfiguration={'OutputLocation': ATHENA_S3_BUCKET,}
    )
    logger.info ('MSCK REPAIR AWS_APPLICATION_TABLE: %s', response)
    response = athena.start_query_execution(
        QueryExecutionContext={'Database': DATABASE,},        
        QueryString='MSCK REPAIR TABLE ' +DATABASE + '.' +AWS_AWS_COMPONENT_TABLE,
        ResultConfiguration={'OutputLocation': ATHENA_S3_BUCKET,}
    )
    logger.info ('MSCK REPAIR AWS_AWS_COMPONENT_TABLE: %s', response)
    response = athena.start_query_execution(
        QueryExecutionContext={'Database': DATABASE,},        
        QueryString='MSCK REPAIR TABLE ' +DATABASE + '.' +AWS_COMPLIANCE_ITEM_TABLE,
        ResultConfiguration={'OutputLocation': ATHENA_S3_BUCKET,}
    )
    logger.info ('MSCK REPAIR AWS_COMPLIANCE_ITEM_TABLE: %s', response)
    response = athena.start_query_execution(
        QueryExecutionContext={'Database': DATABASE,},        
        QueryString='MSCK REPAIR TABLE ' +DATABASE + '.' +AWS_CONFIG_SNAPSHOT_TABLE,
        ResultConfiguration={'OutputLocation': ATHENA_S3_BUCKET,}
    )
    logger.info ('MSCK REPAIR AWS_CONFIG_SNAPSHOT_TABLE: %s', response)
    response = athena.start_query_execution(
        QueryExecutionContext={'Database': DATABASE,},        
        QueryString='MSCK REPAIR TABLE ' +DATABASE + '.' +AWS_INSTANCE_DETAILED_INFORMATION_TABLE,
        ResultConfiguration={'OutputLocation': ATHENA_S3_BUCKET,}
    )
    logger.info ('MSCK REPAIR AWS_INSTANCE_DETAILED_INFORMATION_TABLE: %s', response)
    response = athena.start_query_execution(
        QueryExecutionContext={'Database': DATABASE,},        
        QueryString='MSCK REPAIR TABLE ' +DATABASE + '.' +AWS_INSTANCE_INFORMATION_TABLE,
        ResultConfiguration={'OutputLocation': ATHENA_S3_BUCKET,}
    )
    logger.info ('MSCK REPAIR AWS_INSTANCE_INFORMATION_TABLE: %s', response)
    response = athena.start_query_execution(
        QueryExecutionContext={'Database': DATABASE,},        
        QueryString='MSCK REPAIR TABLE ' +DATABASE + '.' +AWS_NETWORK_TABLE,
        ResultConfiguration={'OutputLocation': ATHENA_S3_BUCKET,}
    )
    logger.info ('MSCK REPAIR AWS_NETWORK_TABLE: %s', response)
    response = athena.start_query_execution(
        QueryExecutionContext={'Database': DATABASE,},        
        QueryString='MSCK REPAIR TABLE ' +DATABASE + '.' +AWS_PATCH_SUMMARY_TABLE,
        ResultConfiguration={'OutputLocation': ATHENA_S3_BUCKET,}
    )
    logger.info ('MSCK REPAIR AWS_PATCH_SUMMARY_TABLE: %s', response)
    response = athena.start_query_execution(
        QueryExecutionContext={'Database': DATABASE,},        
        QueryString='MSCK REPAIR TABLE ' +DATABASE + '.' +AWS_RESOURCE_GROUP_TABLE,
        ResultConfiguration={'OutputLocation': ATHENA_S3_BUCKET,}
    )
    logger.info ('MSCK REPAIR AWS_RESOURCE_GROUP_TABLE: %s', response)
    response = athena.start_query_execution(
        QueryExecutionContext={'Database': DATABASE,},        
        QueryString='MSCK REPAIR TABLE ' +DATABASE + '.' +AWS_SERVICE_TABLE,
        ResultConfiguration={'OutputLocation': ATHENA_S3_BUCKET,}
    )
    logger.info ('MSCK REPAIR AWS_SERVICE_TABLE: %s', response)
    response = athena.start_query_execution(
        QueryExecutionContext={'Database': DATABASE,},        
        QueryString='MSCK REPAIR TABLE ' +DATABASE + '.' +AWS_TAG_TABLE,
        ResultConfiguration={'OutputLocation': ATHENA_S3_BUCKET,}
    )
    logger.info ('MSCK REPAIR AWS_TAG_TABLE: %s', response)
    response = athena.start_query_execution(
        QueryExecutionContext={'Database': DATABASE,},        
        QueryString='MSCK REPAIR TABLE ' +DATABASE + '.' +AWS_WINDOWS_ROLE_TABLE,
        ResultConfiguration={'OutputLocation': ATHENA_S3_BUCKET,}
    )
    logger.info ('MSCK REPAIR AWS_WINDOWS_ROLE_TABLE: %s', response)
    response = athena.start_query_execution(
        QueryExecutionContext={'Database': DATABASE,},        
        QueryString='MSCK REPAIR TABLE ' +DATABASE + '.' +AWS_WINDOWS_UPDATE_TABLE,
        ResultConfiguration={'OutputLocation': ATHENA_S3_BUCKET,}
    )
    logger.info ('MSCK REPAIR AWS_WINDOWS_UPDATE_TABLE: %s', response)

    # Managed Instance Compliance Check View
    response = athena.start_query_execution(
        QueryExecutionContext={
            'Database': DATABASE,
        },        
        QueryString="""
            CREATE OR REPLACE VIEW %s AS 
            SELECT MAX(dt) as ConfigMICDate, 
            MAX(configurationItem.awsaccountid) as ConfigMICAccountID, 
            MAX(configurationItem.awsregion) as ConfigMICRegion, 
            split(configurationItem.resourceid,'/')[2] as ConfigMICInstanceID, 
            MAX(instance.tags['name']) as ConfigMICName,
            MAX(json_extract_scalar(instance.configuration, '$.state.name')) as ConfigMICState,
            MAX(json_extract_scalar(regexp_extract(configurationItem.configuration, '\\{[^}{.]*ec2-instance-managed-by-systems-manager[^}.]*\\}'), '$.compliancetype')) as ConfigMICComplianceStatus
            FROM %s.%s
            CROSS JOIN UNNEST(configurationitems) AS t1(configurationItem)
            CROSS JOIN UNNEST(configurationitems) AS t2(instance)
            WHERE regexp_like(configurationItem.configuration, '\\{[^}{.]*ec2-instance-managed-by-systems-manager[^}.]*\\}')
            AND configurationItem.resourcetype = 'AWS::Config::ResourceCompliance'
            AND t2.instance.resourceID = split(configurationItem.resourceid,'/')[2]
            GROUP BY split(configurationItem.resourceid,'/')[2]""" % (CONFIGMIC_TABLE, DATABASE, AWS_CONFIG_SNAPSHOT_TABLE),
        ResultConfiguration={
            'OutputLocation': ATHENA_S3_BUCKET,
        }
    )
    logger.info ('Create configmic view: %s', response)

    # Patch Compliance Check View
    response = athena.start_query_execution(
        QueryExecutionContext={
            'Database': DATABASE,
        },        
        QueryString="""
            CREATE OR REPLACE VIEW %s AS
            SELECT MAX(dt) as ConfigPCDate,
            split(configurationItem.resourceid,'/')[3] as ConfigPCInstanceID,
            MAX(json_extract_scalar(regexp_extract(configurationItem.configuration, '\\{[^}{.]*ec2-managedinstance-patch-compliance-status-check[^}.]*\\}'), '$.compliancetype')) as ConfigPCStatus
            FROM %s.%s
            CROSS JOIN UNNEST(configurationitems) AS t1(configurationItem)
            WHERE regexp_like(configurationItem.configuration, '\\{[^}{.]*ec2-managedinstance-patch-compliance-status-check[^}.]*\\}')
            AND configurationItem.resourcetype = 'AWS::Config::ResourceCompliance'
            GROUP BY split(configurationItem.resourceid,'/')[3]
            ORDER BY MAX(dt) DESC""" % (CONFIGPC_TABLE, DATABASE, AWS_CONFIG_SNAPSHOT_TABLE),
        ResultConfiguration={
            'OutputLocation': ATHENA_S3_BUCKET,
        }
    )
    logger.info ('Create configpc view: %s', response)

    # Individual Patches View
    response = athena.start_query_execution(
        QueryExecutionContext={
            'Database': DATABASE,
        },        
        QueryString="""
            CREATE OR REPLACE VIEW %s AS
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
            FROM %s.%s
            WHERE compliancetype = 'Patch'""" % (PATCH_TABLE, DATABASE, AWS_COMPLIANCE_ITEM_TABLE),
        ResultConfiguration={
            'OutputLocation': ATHENA_S3_BUCKET,
        }
    )
    logger.info ('Create patch view: %s', response)        
    
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
                'Principal': 'arn:aws:quicksight:' +REGION + ':' +ACCOUNT_ID + ':user/default/' +QUICKSIGHT_USER,
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

    # Create QuickSight Data Set
    response = client.create_data_set(
        AwsAccountId=ACCOUNT_ID,
        DataSetId='patchComplianceDataSet',
        Name='Patch Compliance Data Set',   
        Permissions=[
            {
                'Principal': 'arn:aws:quicksight:' +REGION + ':' +ACCOUNT_ID + ':user/default/' +QUICKSIGHT_USER,
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
            "instanceinformationphysicaltable": {
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
            "networkphysicaltable": {
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
            "instancedetailedinformationphysicaltable": {
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
            "patchsummaryphysicaltable": {
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
            "configpcjoinlogicaltable": {
                "Alias": "configpcjoin",
                "DataTransforms": [
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
                        "ProjectOperation": {
                            "ProjectedColumns": [
                                "configmicdate",
                                "configmicaccountid",
                                "configmicregion",
                                "configmicinstanceid",
                                "configmicname",
                                "configmicstate",
                                "configmiccompliancestatus",
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
                                "patchsummaryoperationenddatetime",
                                "patchsummaryoperationstartdatetime",
                                "patchsummarycapturedatetime",
                                "instancedetailedcapturedatetime",
                                "instanceinformationcapturedatetime",
                                "patchexecutiondatetime",
                                "patchcapturedatetime",
                                "patchinstalleddatetime"
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
            "patchsummaryjoinlogicaltable": {
                "Alias": "patchsummaryjoin",
                "Source": {
                    "JoinInstruction": {
                        "LeftOperand": "configmiclogicaltable",
                        "RightOperand": "patchsummarylogicaltable",
                        "Type": "LEFT",
                        "OnClause": "{configmicinstanceid} = {patchsummaryresourceid}"
                    }
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
            "configpclogicaltable": {
                "Alias": "configpc",
                "Source": {
                    "PhysicalTableId": "configpcphysicaltable"
                }
            },
            "instanceinformationjoinlogicaltable": {
                "Alias": "instanceinformationjoin",
                "Source": {
                    "JoinInstruction": {
                        "LeftOperand": "instancedetailedjoinlogicaltable",
                        "RightOperand": "instanceinformationlogicaltable",
                        "Type": "LEFT",
                        "OnClause": "{configmicinstanceid} = {instanceinformationinstanceid}"
                    }
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
                    "PhysicalTableId": "instancedetailedinformationphysicaltable"
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
                    "PhysicalTableId": "instanceinformationphysicaltable"
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
                    "PhysicalTableId": "networkphysicaltable"
                }
            },
            "patchlogicaltable": {
                "Alias": "patch",
                "Source": {
                    "PhysicalTableId": "patchphysicaltable"
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
                    "PhysicalTableId": "patchsummaryphysicaltable"
                }
            }
        },
        ImportMode='SPICE',
    )
    logger.info ('Create Data Set: %s', response)
    patchingDataset = response['Arn']

    # Create QuickSight Data Set
    response = client.create_data_set(
        AwsAccountId=ACCOUNT_ID,
        DataSetId='patchComplianceByTagDataSet',
        Name='Patch Compliance by Tag', 
        Permissions=[
            {
                'Principal': 'arn:aws:quicksight:' +REGION + ':' +ACCOUNT_ID + ':user/default/' +QUICKSIGHT_USER,
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
            "04ac0f61-12fc-49d6-9a29-2272a0fe2bac": {
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
            "7e681e98-c31e-4981-885d-d1a8ee2f1c92": {
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
            "baf6960a-ceb9-472d-aeb4-02ed286aeb2a": {
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
            },
            "f8b3dc52-ef5f-4574-ac85-a3e9a0b335b5": {
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
            }
        },

        LogicalTableMap={
            "09f55a59-4d04-405a-8702-5422a22b1c01": {
                "Alias": "Intermediate Table (3)",
                "DataTransforms": [
                    {
                        "CreateColumnsOperation": {
                            "Columns": [
                                {
                                    "ColumnName": "patchsummaryoperationenddatetime",
                                    "ColumnId": "e887ad3f-7cf3-46ed-9988-55f7a0c347bc",
                                    "Expression": "ifelse(strlen({patchsummaryoperationendtime})>0,parseDate(replace(substring({patchsummaryoperationendtime},1,19),'T',\" \"),'yyyy-MM-dd HH:mm:ss'),NULL)"
                                }
                            ]
                        }
                    },
                    {
                        "CreateColumnsOperation": {
                            "Columns": [
                                {
                                    "ColumnName": "patchsummaryoperationstartdatetime",
                                    "ColumnId": "b2e18099-666d-4cb0-afea-757270ac3e39",
                                    "Expression": "ifelse(strlen({patchsummaryoperationstarttime})>0,parseDate(replace(substring({patchsummaryoperationstarttime},1,19),'T',\" \"),'yyyy-MM-dd HH:mm:ss'),NULL)\n"
                                }
                            ]
                        }
                    },
                    {
                        "CreateColumnsOperation": {
                            "Columns": [
                                {
                                    "ColumnName": "patchsummarycapturedatetime",
                                    "ColumnId": "499fe046-c39a-4d67-b4ac-f50ac15b2bde",
                                    "Expression": "ifelse(strlen({patchsummarycapturetime})>0,parseDate(replace(substring({patchsummarycapturetime},1,19),'T',\" \"),'yyyy-MM-dd HH:mm:ss'),NULL)"
                                }
                            ]
                        }
                    },
                    {
                        "CreateColumnsOperation": {
                            "Columns": [
                                {
                                    "ColumnName": "tagcaptureDatetime",
                                    "ColumnId": "81195f56-6906-494b-a5d1-dc5000f8d0fc",
                                    "Expression": "ifelse(strlen({tagcapturetime})>0,parseDate(replace(substring({tagcapturetime},1,19),'T',\" \"),'yyyy-MM-dd HH:mm:ss'),NULL)\n"
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
                                "tagkey",
                                "tagvalue",
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
                                "configpcstatus",
                                "patchsummaryoperationenddatetime",
                                "patchsummaryoperationstartdatetime",
                                "patchsummarycapturedatetime",
                                "tagcaptureDatetime"
                            ]
                        }
                    }
                ],
                "Source": {
                    "JoinInstruction": {
                        "LeftOperand": "6b336da4-b913-43f7-98d1-4db982f02532",
                        "RightOperand": "471badba-9b0a-44bc-a4b9-9a70f6115f43",
                        "Type": "LEFT",
                        "OnClause": "{configmicinstanceid} = {configpcinstanceid}"
                    }
                }
            },
            "40ef57bc-0a4c-4b0a-a62c-54129aaa5cd0": {
                "Alias": "Intermediate Table",
                "Source": {
                    "JoinInstruction": {
                        "LeftOperand": "d3362840-7024-4f9e-a0ed-669bbe6cb671",
                        "RightOperand": "99a0de82-a57f-441c-9b83-11649f9cad91",
                        "Type": "LEFT",
                        "OnClause": "{configmicinstanceid} = {tagresourceid}"
                    }
                }
            },
            "471badba-9b0a-44bc-a4b9-9a70f6115f43": {
                "Alias": "configpc",
                "Source": {
                    "PhysicalTableId": "04ac0f61-12fc-49d6-9a29-2272a0fe2bac"
                }
            },
            "6b336da4-b913-43f7-98d1-4db982f02532": {
                "Alias": "Intermediate Table (2)",
                "Source": {
                    "JoinInstruction": {
                        "LeftOperand": "40ef57bc-0a4c-4b0a-a62c-54129aaa5cd0",
                        "RightOperand": "d82acda3-f161-47a9-b710-fd4f2a32eb2c",
                        "Type": "LEFT",
                        "OnClause": "{configmicinstanceid} = {patchsummaryresourceid}"
                    }
                }
            },
            "99a0de82-a57f-441c-9b83-11649f9cad91": {
                "Alias": "aws_tag",
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
                    "PhysicalTableId": "7e681e98-c31e-4981-885d-d1a8ee2f1c92"
                }
            },
            "d3362840-7024-4f9e-a0ed-669bbe6cb671": {
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
                    "PhysicalTableId": "f8b3dc52-ef5f-4574-ac85-a3e9a0b335b5"
                }
            },
            "d82acda3-f161-47a9-b710-fd4f2a32eb2c": {
                "Alias": "aws_patch_summary",
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
                            "ColumnName": "patchsummaryinstalledpendingrebootcount",
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
                    "PhysicalTableId": "baf6960a-ceb9-472d-aeb4-02ed286aeb2a"
                }
            }
        },
        ImportMode='SPICE',
    )
    logger.info ('Create Data Set: %s', response)  
    patchingTagDataset = response['Arn']  

    responseData = {}
    responseData['patchingDataset'] = patchingDataset    
    responseData['patchingTagDataset'] = patchingTagDataset
    cfnresponse.send(event, context, cfnresponse.SUCCESS, responseData, "CustomResourcePhysicalID")