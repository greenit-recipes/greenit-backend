from django.contrib import admin

from user.models import User
from utils.mixin import ExportCsvMixin

# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin, ExportCsvMixin):
    date_hierarchy = 'created_at'
    list_filter = ("is_follow_newsletter",)
    list_display = (
        'id',
        'username',
        'email',
        'is_follow_newsletter',
    )
    actions = ["export_as_csv"]
    search_fields = ['id', 'username', 'email']