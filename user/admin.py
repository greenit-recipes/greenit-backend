from django.contrib import admin

from user.models import User
from utils.mixin import ExportCsvMixin

# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin, ExportCsvMixin):
    date_hierarchy = 'created_at'
    list_filter = ("is_follow_newsletter", "is_creator_profil")
    list_display = (
        'id',
        'username',
        'email',
        'is_follow_newsletter',
        'id_facebook',
        'is_creator_profil',
        'created_at',
        'id_google',
    )
    ordering = ('-created_at',)
    actions = ["export_as_csv"]
    search_fields = ['id', 'username', 'email']
