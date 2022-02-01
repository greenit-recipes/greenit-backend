from django.contrib import admin

from ingredient.models import Ingredient, IngredientAmount
from utils.mixin import ExportCsvMixin

# Register your models here.


class IngredientAdmin(admin.ModelAdmin, ExportCsvMixin):
    search_fields = ["name"]
    actions = ["export_as_csv"]
    pass


admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(IngredientAmount, IngredientAdmin)
