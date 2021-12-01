from django.contrib import admin

from user.models import User
from utils.mixin import ExportCsvMixin

# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_filter = ("is_follow_newsletter",)
    actions = ["export_as_csv"]