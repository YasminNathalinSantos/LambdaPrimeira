import json
from funcaoseparada import exibirLog

def lambda_handler(event, context):
    exibirLog(event)

    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }