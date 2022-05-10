import graphene

from order.models import Order


class OrderInput(graphene.InputObjectType):
    firstName = graphene.String(required=True)
    lastName = graphene.String(required=True)
    email = graphene.String(required=True)
    adressse = graphene.String(required=True)
    postalCode = graphene.String(required=True)
    city = graphene.String(required=True)
    complementAdresse = graphene.String(required=True)
    phone = graphene.String(required=True)

class CreateOrder(graphene.Mutation):
    class Arguments:
        data = OrderInput(required=True)

    success = graphene.Boolean()


    def mutate(root, info, data):
        print('data', data)
        try:
            Order.objects.create(**data)
            return CreateOrder(success=True)
        except Exception as e:
            print(e)
            return CreateOrder(success=False)

