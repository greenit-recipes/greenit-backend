from django.contrib import admin
from tag.models import Tag, Category

# Register your models here.


class TagAdmin(admin.ModelAdmin):
    pass


admin.site.register(Tag, TagAdmin)
admin.site.register(Category, TagAdmin)
