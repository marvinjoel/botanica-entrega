from django.contrib import admin

from plantas.models import PlantasModels


admin.site.register(PlantasModels)
# @admin.register(PlantasModels)
# class PlantasAdmin(admin.ModelAdmin):
#     list_display = ['name','photo','link']
