from django.contrib import admin
from .models import Storehouse, StorehouseItem


class StorehouseItemAdmin(admin.TabularInline):
    model = StorehouseItem
    raw_id_fields = ['product']


class StorehouseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created', 'updated']
    list_filter = ['updated']
    inlines = [StorehouseItemAdmin]


admin.site.register(Storehouse, StorehouseAdmin)
