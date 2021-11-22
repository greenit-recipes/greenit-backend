import graphene
from graphene_django import DjangoObjectType

from user.type import UserType
from .models import CommentRecipe


class CommentType(DjangoObjectType):
    number_of_likes = graphene.Int()
    is_liked_by_current_user = graphene.Boolean()
        
    @staticmethod
    def resolve_number_of_likes(self, parent):
        return self.likes.count()  
    
    @staticmethod
    def resolve_is_liked_by_current_user(self, info):
        if info.context.user.is_authenticated:
            return self.likes.filter(id=info.context.user.id).exists()
        else:
            return False

    class Meta:
        model = CommentRecipe
        fields = (
            'id',
            'comment',
            'created_at',
            'author'
        )

class CommentConnection(graphene.relay.Connection):
    class Meta:
        node = CommentType
