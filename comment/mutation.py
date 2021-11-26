
import graphene
from comment.models import CommentRecipe

from graphql_jwt.decorators import login_required


class AddCommentToRecipe(graphene.Mutation):
    class Arguments:
        comment = graphene.String(required=True)
        recipeId = graphene.String(required=True)

    success = graphene.Boolean()

    @login_required
    def mutate(root, info, comment, recipeId):
        user = info.context.user
        try:
            recipe = CommentRecipe.objects.create(
                comment=comment,
                recipe_id= recipeId,
                author_id= user.id
            )
            recipe.save()
            return AddCommentToRecipe(success=True)
        except Exception as e:
            print(e)
            return AddCommentToRecipe(success=False)


class AddOrRemoveLikeComment(graphene.Mutation):
    class Arguments:
        commentId = graphene.String(required=True)

    success = graphene.Boolean()

    @login_required
    def mutate(root, info, commentId):
        try:
            comment = CommentRecipe.objects.get(id=commentId)
            user = info.context.user
            if comment.likes.filter(id=user.id).exists():
                comment.likes.remove(user)
            else:
                comment.likes.add(user)

            return AddOrRemoveLikeComment(success=True)
        except Exception as e:
            print(e)
            return AddOrRemoveLikeComment(success=False)
