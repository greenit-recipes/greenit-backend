from tag.models import Category, Tag, Category_Ingredient


def create_tag(name):
    return Tag.objects.create(name=name)


def create_category(name):
    return Category.objects.create(name=name)


def create_category(name):
    return Category_Ingredient.objects.create(name=name)