import json
import graphene
import re

from query import Query
from task_mutations import CreateKanbanTask, DeleteKanbanTask
from category_mutations import CreateKanbanCategory, DeleteKanbanCategory

class KanbanTaskMutation(graphene.ObjectType):
    create_kanban_task = CreateKanbanTask.Field()
    delete_kanban_task = DeleteKanbanTask.Field()
    create_kanban_category = CreateKanbanCategory.Field()
    delete_kanban_category = DeleteKanbanCategory.Field()

schema = graphene.Schema(query=Query, mutation=KanbanTaskMutation)

def lambda_handler(event, context):
    body = json.loads(event['body'])
    variables = {}                      #if the event has no a variables
    if 'variables' in body:
        variables = body['variables']
    
    result = schema.execute(body['query'], variable_values=variables)
    
    if result.errors:
        print(result)
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST, GET'
        },
        'body': json.dumps({'data': result.data})
    }