from django.core.management.base import BaseCommand
import django.contrib.auth
from django.core.management import call_command


class Command(BaseCommand):
    help = 'Populate database'

    def handle(self, *args, **kwargs):
        call_command('flush', '--no-input')

        User = django.contrib.auth.get_user_model()

        # Admin
        userCreated = User.objects.create_user(
            name='admin', password='1234', email='admin@gmail.com', is_superuser=True, is_staff=True)
        self.stdout.write("Admin created successfully")

        # Users
        users = [{
            'name': 'naruto',
        }, {
            'name': 'sasuke',
        }, {
            'name': 'madara',
        }]
        for user in users:
            userName = user.get('name')
            userCreated = User.objects.create_user(
                name=userName, password='1234', email=userName+'@gmail.com', is_superuser=False, is_staff=False)
            userCreated.save()
        self.stdout.write("Users created successfully")

        # If u want to add some data for local after ur created ur feature use --> "manage.py dumpdata > data.json"
        # https://docs.djangoproject.com/en/3.2/howto/initial-data/#providing-data-with-fixtures

        # Data
        # Respect the order
        filesPopulate = ['populate/tag-populate.json',
                         'populate/tagCategory-populate.json',
                         'populate/ingredient-populate.json',
                         'populate/recipe-populate.json',
                         'populate/ingredientAmount-populate.json']

        for filePopulate in filesPopulate:
            call_command('loaddata', filePopulate)
