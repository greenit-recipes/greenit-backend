from django.contrib import admin

# Register your models here.
from substance.models import Substance
from utils.mixin import ExportCsvMixin

# Register your models here.


class SubstanceAdmin(admin.ModelAdmin, ExportCsvMixin):
    search_fields = ["name"]
    actions = ["export_as_csv"]    

    pass


admin.site.register(Substance, SubstanceAdmin)
