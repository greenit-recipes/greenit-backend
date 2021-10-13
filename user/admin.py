from django.contrib import admin
from django.apps import apps

from user.models import User

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, UserAdmin)

app = apps.get_app_config('graphql_auth')

for model_name, model in app.models.items():
    admin.site.register(model)
