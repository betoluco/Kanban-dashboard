import json
import graphene

from query import Query
from mutations import KanbanTaskMutation

schema = graphene.Schema(query=Query, mutation=KanbanTaskMutation)

def lambda_handler(event, context):
    result = schema.execute(event["queryStringParameters"]['query'])

    return {
        'statusCode': 200,
        'body': json.dumps(result.data)
    }   