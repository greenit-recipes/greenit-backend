from django.contrib import admin
from comment.models import CommentRecipe
# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = (
        'id',
        'comment',
        'author_id',
        'recipe_id',
        'created_at',
    )
    search_fields = ['id', 'comment', 'author__id', 'author__username']
    pass


admin.site.register(CommentRecipe, CommentAdmin)
