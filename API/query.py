import boto3
import graphene
import os

from kanban_task import KanbanTask 
from kanban_category import KanbanCategory

dynamodb = boto3.resource('dynamodb')
tasks_table = dynamodb.Table(os.environ['TASKS_TABLE'])
categories_table = dynamodb.Table(os.environ['CATEGORIES_TABLE'])

class Query(graphene.ObjectType):
    kanban_tasks_list = graphene.List(KanbanTask)
    kanban_categories_list = graphene.List(KanbanCategory)
    
    def resolve_kanban_tasks_list(root, info):
        try: 
            task_table_items = tasks_table.scan()
            return task_table_items['Items']
        except Exception as e:
            print(f"Error scanning table: {str(e)}")
            
    def resolve_kanban_categories_list(root, info):
        try: 
            categories_table_items = categories_table.scan()
            return categories_table_items['Items']
        except Exception as e:
            print(f"Error scanning table: {str(e)}")