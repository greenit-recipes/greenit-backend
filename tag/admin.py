from django.contrib import admin

from tag.models import Category, Tag
from utils.mixin import ExportCsvMixin

# Register your models here.


class TagAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_per_page = 500
    search_fields = ["name"]
    actions = ["export_as_csv"]


admin.site.register(Tag, TagAdmin)
admin.site.register(Category, TagAdmin)
