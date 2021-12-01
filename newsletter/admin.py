from django.contrib import admin

from newsletter.models import NewsLetter
from utils.mixin import ExportCsvMixin
# Register your models here.

@admin.register(NewsLetter)
class NewsLetterAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ("id", "email")
    actions = ["export_as_csv"]

