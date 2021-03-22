from django import forms
from django.contrib import admin
from django_admin_json_editor import JSONEditorWidget

from recipe.models import Recipe


class IngredientAmountInline(admin.StackedInline):
    model = Recipe.ingredients.through


class UtensilAmountInline(admin.StackedInline):
    model = Recipe.utensils.through


INSTRUCTION_SCHEMA = {
    'type': 'array',
    'title': 'Instructions',
    'items': {
        'type': 'object',
        'required': ['content', 'index', 'timestamp'],
        'properties': {
            'content': {
                'title': 'Some text',
                'type': 'string',
                'format': 'textarea',
            },
            'index': {
                'title': 'Index',
                'type': 'integer',
            },
            'timestamp': {
                'title': 'Timestamp',
                'type': 'string',
            },
        },
    },
}


class RecipeAdminForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'
        widgets = {
            'instructions': JSONEditorWidget(INSTRUCTION_SCHEMA, collapsed=False)
        }


class RecipeAdmin(admin.ModelAdmin):
    inlines = (
        IngredientAmountInline,
        UtensilAmountInline,
    )
    list_display = (
        'name',
        'difficulty',
        'duration',
        'rating',
    )
    form = RecipeAdminForm


admin.site.register(Recipe, RecipeAdmin)
