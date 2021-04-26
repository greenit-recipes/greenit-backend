from utensil.models import Utensil


def create_utensil(name):
    return Utensil.objects.create(name=name)
