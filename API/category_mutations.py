import boto3
import graphene
import os
import json
from datetime import datetime

from kanban_category import KanbanCategory

dynamodb = boto3.client('dynamodb')

class CreateKanbanCategory(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
    
    ok = graphene.Boolean()
    kanban_category = graphene.Field(lambda: KanbanCategory)
    
    def mutate(root, info, id):
        try:
            response = dynamodb.put_item(
                TableName=os.environ['CATEGORIES_TABLE'],
                Item={
                    'id': {'S': id}
                }
            )
            kanban_category = KanbanCategory(id=id)
            ok = True
            return CreateKanbanCategory(kanban_category=kanban_category, ok=ok)
        except Exception as e:
            print(f"Error scanning table: {str(e)}")
            
            
class DeleteKanbanCategory(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
    
    ok = graphene.Boolean()
    kanban_category = graphene.Field(lambda: KanbanCategory)
    
    def mutate(root, info, id):
        try:
            response = dynamodb.delete_item(
                TableName=os.environ['CATEGORIES_TABLE'], 
                Key={
                    'id': {'S': id}
                }
            )
            kanban_category = KanbanCategory(id=id)
            ok = True
            return DeleteKanbanCategory(kanban_category=kanban_category, ok=ok)
        except Exception as e:
            print(f"Error scanning table: {str(e)}")