from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'city',
                    'address', 'phone', 'paid',
                    'created']
    list_display_links = ('id', 'first_name')
    list_filter = ['paid', 'created']
    inlines = [OrderItemInline]
