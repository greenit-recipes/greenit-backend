from user.models import User


def create_user(name):
    return User.objects.create(name=name)
