from django.contrib import admin
from ingredient.models import Ingredient, IngredientAmount

# Register your models here.


class IngredientAdmin(admin.ModelAdmin):
    pass


admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(IngredientAmount, IngredientAdmin)
