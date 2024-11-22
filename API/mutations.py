import boto3
import graphene
import os
import random
import json

from kanban_task import KanbanTask 

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

class CreateKanbanTask(graphene.Mutation):
    class Arguments:
        PK = graphene.String()
        title = graphene.String()
        description = graphene.String()
        status = graphene.String()
    
    ok = graphene.Boolean()
    kanban_task = graphene.Field(lambda: KanbanTask)
    
    def mutate(root, info, title, description, status):
        try:
            PK = title + str(random.randrange(1000000))
            response = table.put_item(Item= {
                'PK':PK,
                'title':title, 
                'description':description, 
                'status':status 
            })
            kanban_task = KanbanTask(
                PK=PK,
                title=title, 
                description=description, 
                status=status
            )
            ok = True
            return CreateKanbanTask(kanban_task=kanban_task, ok=ok)
        except Exception as e:
            print(f"Error scanning table: {str(e)}")

class KanbanTaskMutation(graphene.ObjectType):
    create_kanban_task = CreateKanbanTask.Field()