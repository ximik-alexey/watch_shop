from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'order_processed','first_name', 'address',
                    'city', 'created', 'updated']
    list_filter = ['order_processed','created', 'updated']
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)
