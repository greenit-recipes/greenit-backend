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
    description = forms.CharField( widget=forms.Textarea )
    text_associate = forms.CharField( widget=forms.Textarea, required=False )
    class Meta:
        model = Recipe
        fields = '__all__'
        exclude = ['url_id', 'rating']
        widgets = {
            'instructions': JSONEditorWidget(INSTRUCTION_SCHEMA, collapsed=False)
        }


class RecipeAdmin(admin.ModelAdmin):
    inlines = (
        IngredientAmountInline,
        UtensilAmountInline,
    )
    date_hierarchy = 'created_at'
    list_display = (
        'id',
        'name',
        'difficulty',
        'author',
        'rating',
    )
    search_fields = ['id', 'name', 'tags__name', 'author__email', 'ingredients__name', 'category__name']
    form = RecipeAdminForm


admin.site.register(Recipe, RecipeAdmin)
