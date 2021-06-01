from django.core.management.base import BaseCommand
from recipe.models import Recipe


class Command(BaseCommand):
    help = 'Runs the save function assigning url_ids'
    def handle(self, *args, **options):
        for r in Recipe.objects.all():
            r.save()
