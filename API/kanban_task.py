import graphene

class KanbanTask(graphene.ObjectType):
    category =  graphene.String()
    datetime =  graphene.String()
    title = graphene.String()
    description = graphene.String()