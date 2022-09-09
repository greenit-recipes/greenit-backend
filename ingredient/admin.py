from django.contrib import admin

from ingredient.models import Ingredient, IngredientAmount, IngredientAtHomeUser, IngredientShoppingListUser
from utils.mixin import ExportCsvMixin


# Register your models here.


class IngredientAdmin(admin.ModelAdmin, ExportCsvMixin):
    search_fields = ["name"]
    actions = ["export_as_csv"]
    list_display = (
        'name',
        'nbr_of_liste_de_course',
        'nbr_of_ingredient_chez_moi',
    )

    def nbr_of_liste_de_course(self, obj):
        return len(IngredientShoppingListUser.objects.filter(ingredient=obj.id))

    def nbr_of_ingredient_chez_moi(self, obj):
        return len(IngredientAtHomeUser.objects.filter(ingredient=obj.id))


class IngredientAmountAdmin(admin.ModelAdmin, ExportCsvMixin):
    search_fields = ["name"]
    actions = ["export_as_csv"]


admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(IngredientAmount, IngredientAmountAdmin)
