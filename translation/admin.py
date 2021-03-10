from django.contrib import admin

from translation.models import Translation

# Register your models here.


class TranslationAdmin(admin.ModelAdmin):
    pass


admin.site.register(Translation, TranslationAdmin)
