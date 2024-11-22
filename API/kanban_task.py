import graphene

class KanbanTask(graphene.ObjectType):
    PK =  graphene.String()
    SK =  graphene.String()
    title = graphene.String()
    description = graphene.String()