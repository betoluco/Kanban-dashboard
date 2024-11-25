import boto3
import graphene
import os
import json
from datetime import datetime

from kanban_task import KanbanTask 

dynamodb = boto3.client('dynamodb')

class CreateKanbanTask(graphene.Mutation):
    class Arguments:
        category = graphene.String()
        title = graphene.String()
        description = graphene.String()
    
    ok = graphene.Boolean()
    kanban_task = graphene.Field(lambda: KanbanTask)
    
    def mutate(root, info, category, title, description):
        now = str(datetime.now())
        try:
            response = dynamodb.put_item(
                TableName=os.environ['TASKS_TABLE'],
                Item={
                    'category': {'S': category},
                    'datetime': {'S': now},
                    'title': {'S': title},
                    'description': {'S': description}
                }
            )
            kanban_task = KanbanTask(
                category=category,
                datetime=datetime,
                title=title, 
                description=description, 
            )
            ok = True
            return CreateKanbanTask(kanban_task=kanban_task, ok=ok)
        except Exception as e:
            print(f"Error scanning table: {str(e)}")
            
            
class DeleteKanbanTask(graphene.Mutation):
    class Arguments:
        category = graphene.String()
        datetime = graphene.String()
    
    ok = graphene.Boolean()
    
    def mutate(root, info, category, datetime):
        try:
            response = dynamodb.delete_item(
                TableName=os.environ['TASKS_TABLE'], 
                Key={
                    'category': {'S': category}, 
                    'datetime': {'S': datetime}
                }
            )
            ok = True
            return DeleteKanbanTask(ok=ok)
        except Exception as e:
            print(f"Error scanning table: {str(e)}")

class KanbanTaskMutation(graphene.ObjectType):
    create_kanban_task = CreateKanbanTask.Field()
    delete_kanban_task = DeleteKanbanTask.Field()