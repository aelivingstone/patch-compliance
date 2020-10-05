import boto3
import json
import logging
import cfnresponse

ssm = boto3.client('ssm')
ec2 = boto3.client('ec2')
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context): 
    # set token to empty string
    token = ''

    # CFN Response
    responseValue = 0

    
    while True:
        # Limit to 1,000 due to ec2.create_tags limit
        response = ssm.describe_instance_information(
            Filters=[{'Key': 'PlatformTypes','Values': ['Linux']},],
            MaxResults=50,
            NextToken = token
        )
        
        # Create empty instances array
        instances = []

        for instanceInfo in response['InstanceInformationList']:
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
            
        # Constraints: Up to 1000 resource IDs. We recommend breaking up this request into smaller batches.
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