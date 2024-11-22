import graphene

class KanbanTask(graphene.ObjectType):
    title = graphene.String()
    description = graphene.String()
    status = graphene.String()  # Example: "To Do", "In Progress", "Done"