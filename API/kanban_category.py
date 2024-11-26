import graphene

class KanbanCategory(graphene.ObjectType):
    name =  graphene.String()