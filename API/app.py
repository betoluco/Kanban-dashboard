import json
from graphene import ObjectType, String, Schema, List
import boto3
import os

class KanbanTask(ObjectType):
    title = String()
    description = String()
    status = String()  # Example: "To Do", "In Progress", "Done"

class Query(ObjectType):
    kanbanTasksList = List(KanbanTask)
    hello = String(name=String(default_value="stranger"))
    goodbye = String()
    
    def resolve_kanbanTasksList(root, info):
        try: 
            response = table.scan()
            return response['Items']
        except Exception as e:
            print(f"Error scanning table: {str(e)}")
    
    def resolve_hello(root, info, name):
        return f'Hello {name}!'

    def resolve_goodbye(root, info):
        return 'See ya!'

schema = Schema(query=Query)
dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    
    global table
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])
    
    result = schema.execute(event["queryStringParameters"]['query'])

    return {
        'statusCode': 200,
        'body': json.dumps(result.data)
    }