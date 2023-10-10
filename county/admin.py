from django.contrib import admin
from .models import *

class SubCountyInline(admin.TabularInline):
    model= SubCounty
    extra= 1

class CountyAdmin(admin.ModelAdmin):
    inlines= [SubCountyInline]


class WardInline(admin.TabularInline):
    model= Ward
    extra= 1

class SubCountyAdmin(admin.ModelAdmin):
    inlines= [WardInline]

class CommunityAreaInline(admin.TabularInline):
    model= CommunityArea
    extra= 1

class WardAdmin(admin.ModelAdmin):
    inlines= [CommunityAreaInline]

class VillageInline(admin.TabularInline):
    model= Village
    extra= 1

class CommunityAreaAdmin(admin.ModelAdmin):
    inlines=[VillageInline]


# Register your models here.
admin.site.register(County, CountyAdmin)
admin.site.register(SubCounty,SubCountyAdmin)
admin.site.register(Ward, WardAdmin)
admin.site.register(CommunityArea, CommunityAreaAdmin)
admin.site.register(Village)