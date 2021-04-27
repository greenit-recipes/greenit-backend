from recipe.models import Recipe


def create_recipe(name):
    return Recipe.objects.create(name=name)
