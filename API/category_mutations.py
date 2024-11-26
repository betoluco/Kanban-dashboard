import boto3
import graphene
import os
import json
from datetime import datetime

from kanban_category import KanbanCategory

dynamodb = boto3.client('dynamodb')

class CreateKanbanCategory(graphene.Mutation):
    class Arguments:
        name = graphene.String()
    
    ok = graphene.Boolean()
    kanban_category = graphene.Field(lambda: KanbanCategory)
    
    def mutate(root, info, name):
        try:
            response = dynamodb.put_item(
                TableName=os.environ['CATEGORIES_TABLE'],
                Item={
                    'name': {'S': name}
                }
            )
            kanban_category = KanbanCategory(name=name)
            ok = True
            return CreateKanbanCategory(kanban_category=kanban_category, ok=ok)
        except Exception as e:
            print(f"Error scanning table: {str(e)}")
            
            
class DeleteKanbanCategory(graphene.Mutation):
    class Arguments:
        name = graphene.String()
    
    ok = graphene.Boolean()
    
    def mutate(root, info, name):
        try:
            response = dynamodb.delete_item(
                TableName=os.environ['CATEGORIES_TABLE'], 
                Key={
                    'name': {'S': name}
                }
            )
            ok = True
            return DeleteKanbanCategory(ok=ok)
        except Exception as e:
            print(f"Error scanning table: {str(e)}")