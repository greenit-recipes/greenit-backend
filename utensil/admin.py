from django.contrib import admin

from utensil.models import Utensil, UtensilAmount


class UtensilAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    pass


admin.site.register(Utensil, UtensilAdmin)
admin.site.register(UtensilAmount, UtensilAdmin)
