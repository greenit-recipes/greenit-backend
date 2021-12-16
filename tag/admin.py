from django.contrib import admin

from tag.models import Category, Tag

# Register your models here.


class TagAdmin(admin.ModelAdmin):
    list_per_page = 500
    search_fields = ["name"]


admin.site.register(Tag, TagAdmin)
admin.site.register(Category, TagAdmin)
