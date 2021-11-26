import graphene

from .models import User
from .type import UserType
from graphql_auth import mutations
from graphene_file_upload.scalars import Upload
from graphql_jwt.decorators import login_required

class AuthMutation(graphene.ObjectType):
   register = mutations.Register.Field()
   verify_account = mutations.VerifyAccount.Field()
   update_account = mutations.UpdateAccount.Field()
       
class CreateUser(AuthMutation):
    pass


class UpdateImageAccount(graphene.Mutation):
    
    class Arguments:
        imageProfile = Upload(required=True)

    success = graphene.Boolean()

    @login_required
    def mutate(root, info, imageProfile):
      try:
          user = info.context.user
          userImage = User.objects.get(id=user.id)
          userImage.image_profile=imageProfile[0]
          userImage.save()
          return UpdateImageAccount(success=True)
       
      except Exception as e:
          print(e)
          return UpdateImageAccount(success=False)