from user.models import User


def wcreate_user(name):
    return User.objects.create(name=name)
