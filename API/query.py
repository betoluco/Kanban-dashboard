import boto3
import graphene
import os

from kanban_task import KanbanTask 

dynamodb = boto3.resource('dynamodb')
tasks_table = dynamodb.Table(os.environ['TASKS_TABLE'])
# category_table = dynamodb.Table(os.environ['CATEGORY_TABLE'])

class Query(graphene.ObjectType):
    kanban_tasks_list = graphene.List(KanbanTask)
    # kanban_categories = graphene.String()
    
    def resolve_kanban_tasks_list(root, info):
        try: 
            task_table_items = tasks_table.scan()
            return task_table_items['Items']
        except Exception as e:
            print(f"Error scanning table: {str(e)}")
            
    # def resolve_kanban_category_list(root, info):
        # try: 
        #     # category_table_items = category_table.scan()
        #     return response['Items']
        # except Exception as e:
        #     print(f"Error scanning table: {str(e)}")