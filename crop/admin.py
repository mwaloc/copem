from django.contrib import admin
from .models import *

class CropInline(admin.TabularInline):
    model= Crop
    extra= 1

class CropAdmin(admin.ModelAdmin):
    inlines= [CropInline]

class PlantingCycleInline(admin.TabularInline):
    model= PlantingCycle
    extra= 1

class PlantingCycleAdmin(admin.ModelAdmin):
    inlines= [PlantingCycleInline]

# Register your models here.
admin.site.register(CropCategory, CropAdmin)
admin.site.register(Crop, PlantingCycleAdmin)
admin.site.register(PlantingCycle)

