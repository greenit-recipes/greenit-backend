from tag.models import Tag

def create_tag(name):
    return Tag.objects.create(name=name)
