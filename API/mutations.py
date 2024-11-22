import boto3
import graphene
import os
import json
from datetime import datetime

from kanban_task import KanbanTask 

dynamodb = boto3.client('dynamodb')

class CreateKanbanTask(graphene.Mutation):
    class Arguments:
        PK = graphene.String()
        title = graphene.String()
        description = graphene.String()
    
    ok = graphene.Boolean()
    kanban_task = graphene.Field(lambda: KanbanTask)
    
    def mutate(root, info, PK, title, description):
        SK = str(datetime.now())
        try:
            response = dynamodb.put_item(
                TableName=os.environ['DYNAMODB_TABLE'],
                Item={
                    'PK': {'S': PK},
                    'SK': {'S': SK},
                    'title': {'S': title},
                    'description': {'S': description}
                }
            )
            kanban_task = KanbanTask(
                PK=PK,
                SK=SK,
                title=title, 
                description=description, 
            )
            ok = True
            return CreateKanbanTask(kanban_task=kanban_task, ok=ok)
        except Exception as e:
            print(f"Error scanning table: {str(e)}")
            
            
class DeleteKanbanTask(graphene.Mutation):
    class Arguments:
        PK = graphene.String()
        SK = graphene.String()
    
    ok = graphene.Boolean()
    
    def mutate(root, info, PK, SK):
        try:
            response = dynamodb.delete_item(
                TableName=os.environ['DYNAMODB_TABLE'], 
                Key={
                    'PK': {'S': PK}, 
                    'SK': {'S': SK}
                }
            )
            ok = True
            return DeleteKanbanTask(ok=ok)
        except Exception as e:
            print(f"Error scanning table: {str(e)}")

class KanbanTaskMutation(graphene.ObjectType):
    create_kanban_task = CreateKanbanTask.Field()
    delete_kanban_task = DeleteKanbanTask.Field()