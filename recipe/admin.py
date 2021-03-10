from django.contrib import admin

from recipe.models import Recipe


class IngredientAmountInline(admin.StackedInline):
    model = Recipe.ingredients.through


class UtensilAmountInline(admin.StackedInline):
    model = Recipe.utensils.through


class RecipeAdmin(admin.ModelAdmin):
    inlines = (
        IngredientAmountInline,
        UtensilAmountInline,
    )


admin.site.register(Recipe, RecipeAdmin)
