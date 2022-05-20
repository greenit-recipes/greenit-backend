from django.contrib import admin

# Register your models here.
from django.contrib import admin
from fflags.models import FFlags

from utils.mixin import ExportCsvMixin

# Register your models here.
class FflagsAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = (
        'id',
        'is_active',
        'description',
        'name',
    )
    ordering = ('-created_at',)
    actions = ["export_as_csv"]
    search_fields = ['name']


admin.site.register(FFlags, FflagsAdmin)
