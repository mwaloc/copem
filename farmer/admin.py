from django.contrib import admin
from .models import *
from crop.models import *

class FarmInline(admin.TabularInline):
    model= Farm
    extra= 1

class FarmAdmin(admin.ModelAdmin):
    inlines= [FarmInline]

class Farm2Inline(admin.TabularInline):
    model= PlantingCycle
    extra= 1

class Farm2Admin(admin.ModelAdmin):
    inlines= [Farm2Inline]



# Register your models here.
admin.site.register(Farmer, FarmAdmin)
admin.site.register(Farm, Farm2Admin )
admin.site.register(LandUnit)
