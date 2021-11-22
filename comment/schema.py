
import graphene
from comment.models import CommentRecipe
from comment.mutation import AddCommentToRecipe, AddOrRemoveLikeComment

from comment.type import CommentConnection, CommentType
from django_filters import FilterSet, OrderingFilter


class Query(graphene.ObjectType):
    comments = graphene.relay.ConnectionField(
        CommentConnection, recipeId = graphene.String(required=True)
    )
    
    def resolve_comments(self, info, recipeId=None): # ne marche pas
        CommentRecipe.objects.filter(recipe_id=recipeId).order_by('-created_at')

class Mutation(graphene.ObjectType):
    add_or_remove_like_comment = AddOrRemoveLikeComment.Field()
    add_comment_to_recipe = AddCommentToRecipe.Field()