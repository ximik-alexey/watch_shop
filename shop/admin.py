from django.contrib import admin
from .models import Brand, Product, MechanismType, Glass, WaterResistanceClass


class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


class MechanismTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


class GlassAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


class WaterResistanceClassAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','brand', 'slug', 'price', 'stock', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Brand, BrandAdmin)
admin.site.register(MechanismType, MechanismTypeAdmin)
admin.site.register(Glass, GlassAdmin)
admin.site.register(WaterResistanceClass, WaterResistanceClassAdmin)
admin.site.register(Product, ProductAdmin)
