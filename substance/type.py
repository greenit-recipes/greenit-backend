from graphene_django import DjangoObjectType

from .models import Substance


class SubstanceType(DjangoObjectType):
    class Meta:
        model = Substance
        fields = ('id', 'name', 'group_subs', 'effect')
