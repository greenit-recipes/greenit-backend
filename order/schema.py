


import graphene
from order.models import Order

from order.mutation import CreateOrder
from order.type import OrderType



class Query(graphene.ObjectType):
    all_order = graphene.List(OrderType)

    def resolve_all_order(self, info):
        return Order.objects.getAll()

class Mutation(graphene.ObjectType):
    create_order = CreateOrder.Field()