from django import forms
from django.contrib import admin
from django_admin_json_editor import JSONEditorWidget
from django.contrib.admin.widgets import AutocompleteSelect

from recipe.models import Recipe, Made
from ingredient.models import Ingredient
from utils.mixin import ExportCsvMixin


class IngredientAmountInline(admin.StackedInline):
    autocomplete_fields = ["ingredient"]
    model = Recipe.ingredients.through


class UtensilAmountInline(admin.StackedInline):
    autocomplete_fields = ["utensil"]
    model = Recipe.utensils.through


class RecipeAdminForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea)
    text_associate = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        exclude = ['url_id', 'rating']


class RecipeAdmin(admin.ModelAdmin, ExportCsvMixin):
    inlines = (
        IngredientAmountInline,
        UtensilAmountInline,
    )
    date_hierarchy = 'created_at'
    autocomplete_fields = ["tags", "author", 'substances']
    actions = ["export_as_csv"]
    list_filter = ("is_display_home",)
    ordering = ('-created_at',)
    list_display = (
        'id',
        'name',
        'author',
        'nbr_view',
        'nbr_of_likes',
        'nbr_of_favorites',
        'nbr_of_times_made',
    )
    search_fields = ['name']
    form = RecipeAdminForm

    def nbr_of_likes(self, obj):
        return len(Recipe.objects.get(pk=obj.id).likes.all())

    def nbr_of_favorites(self, obj):
        return len(Recipe.objects.get(pk=obj.id).favorites.all())

    def nbr_of_times_made(self, obj):
        return len(Made.objects.filter(recipe=obj.id))


admin.site.register(Recipe, RecipeAdmin)
