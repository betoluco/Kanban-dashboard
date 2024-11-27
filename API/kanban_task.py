import graphene

class KanbanTask(graphene.ObjectType):
    category =  graphene.String()
    id =  graphene.ID()
    title = graphene.String()
    description = graphene.String()