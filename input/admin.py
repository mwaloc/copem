from django.contrib import admin
from .models import *

class SupplierInline(admin.TabularInline):
    model= InputSupply
    extra= 1

class SupplierAdmin(admin.ModelAdmin):
    inlines= [SupplierInline]

# Register your models here.
admin.site.register(InputCategory)
admin.site.register(InputSupplier, SupplierAdmin)
admin.site.register(InputSupply)
admin.site.register(InputDistribution)