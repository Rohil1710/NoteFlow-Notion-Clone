import boto3
import json

dynamodb_resource = boto3.resource("dynamodb")
data_table = dynamodb_resource.Table("lotion-30139470")

def lambda_handler3(event, context):
    body = json.loads(event["body"])
    id_value = body.get('id')
    email_value = body.get('email')

    try:
        data_table.delete_item(
            Key={'id': id_value, 'email': email_value}
        )

        return {
            "statusCode": 200,
            "body": "success"
        }

    except Exception as exp:
        return {
            "statusCode": 500,
            "body": json.dumps(
                {
                    "message": str(exp)
                }
            )
        }

