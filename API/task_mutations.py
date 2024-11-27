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
                    'id': {'S': now},
                    'title': {'S': title},
                    'description': {'S': description}
                }
            )
            kanban_task = KanbanTask(
                category=category,
                id=id,
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
        id = graphene.ID()
    
    ok = graphene.Boolean()
    kanban_task = graphene.Field(lambda: KanbanTask)
    
    def mutate(root, info, category, id):
        try:
            response = dynamodb.delete_item(
                TableName=os.environ['TASKS_TABLE'], 
                Key={
                    'category': {'S': category}, 
                    'id': {'S': id}
                }
            )
            kanban_task = KanbanTask(
                category=category,
                id=id,
            )
            ok = True
            return DeleteKanbanTask(kanban_task=kanban_task, ok=ok)
        except Exception as e:
            print(f"Error scanning table: {str(e)}")
            