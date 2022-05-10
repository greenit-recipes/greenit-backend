from graphene_django import DjangoObjectType
from order.models import Order

class OrderType(DjangoObjectType):
    class Meta:
        model = Order
        fields = ('id', 'firstName', 'lastName', 'email', 'adresse', 'postalCode', 'city', 'complementAdresse', 'phone')
