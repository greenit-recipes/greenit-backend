from ingredient.models import Ingredient


def create_ingredient(name):
    return Ingredient.objects.create(name=name)
