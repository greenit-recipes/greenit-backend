from django.contrib import admin

from utensil.models import Utensil, UtensilAmount

# Register your models here.


class UtensilAdmin(admin.ModelAdmin):
    pass


admin.site.register(Utensil, UtensilAdmin)
admin.site.register(UtensilAmount, UtensilAdmin)
