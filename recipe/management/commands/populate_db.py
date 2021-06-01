from django.core.management.base import BaseCommand
from recipe.models import Recipe


class Command(BaseCommand):
    def handle(self, *args, **options):
        for r in Recipe.objects.all():
            url_id = Recipe.objects.name
            r.save()
