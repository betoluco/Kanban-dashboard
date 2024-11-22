import boto3
import graphene
import os

from kanban_task import KanbanTask 

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

class Query(graphene.ObjectType):
    kanban_tasks_list = graphene.List(KanbanTask)
    
    def resolve_kanban_tasks_list(root, info):
        try: 
            response = table.scan()
            return response['Items']
        except Exception as e:
            print(f"Error scanning table: {str(e)}")