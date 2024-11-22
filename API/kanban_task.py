import graphene

class KanbanTask(graphene.ObjectType):
    PK =  graphene.String()
    title = graphene.String()
    description = graphene.String()
    status = graphene.String()  # Example: "To Do", "In Progress", "Done"