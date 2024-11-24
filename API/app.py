import json
import graphene

from query import Query
from mutations import KanbanTaskMutation

schema = graphene.Schema(query=Query, mutation=KanbanTaskMutation)

def lambda_handler(event, context):
    result = schema.execute(json.loads(event['body'])['query'])

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST, GET'
        },
        'body': json.dumps({'data': result.data})
    }