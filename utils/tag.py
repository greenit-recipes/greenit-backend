from tag.models import Tag, Category


def create_tag(name):
    return Tag.objects.create(name=name)

def create_category(name):
    return Category.objects.create(name=name)
