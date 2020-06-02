from django.contrib import admin
from .models import Purchase, PurchaseItem


class PurchaseItemAdmin(admin.TabularInline):
    model = PurchaseItem
    raw_id_fields = ['product']


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['id', 'processed', 'created', 'updated']
    list_filter = ['processed', 'updated']
    inlines = [PurchaseItemAdmin]


admin.site.register(Purchase, PurchaseAdmin)
