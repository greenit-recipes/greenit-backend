import graphene
from graphene_django import DjangoObjectType
from .models import FFlags


class FeatureFlagType(DjangoObjectType):
    class Meta:
        model = FFlags
        fields = "__all__"


class Query(graphene.ObjectType):
    feature_flag = graphene.Field(FeatureFlagType, name=graphene.String(required=True))

    def resolve_feature_flag(self, info, name):
        return FFlags.objects.get(name=name)



