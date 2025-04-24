# from django.contrib import admin
# from .models import Order

# @admin.register(Order)
# class OrderAdmin(admin.ModelAdmin):
#     list_display = ('id', 'first_name', 'last_name', 'email', 'city', 'created', 'updated')
#     list_filter = ('created', 'updated', 'city')
#     search_fields = ('first_name', 'last_name', 'email', 'phone_number')
#     ordering = ('-created',)


# admin.site.unregister(Order)

from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    readonly_fields = ('product', 'price', 'quantity', 'personal_text')
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'city', 'created', 'updated')
    list_filter = ('created', 'updated', 'city')
    search_fields = ('first_name', 'last_name', 'email', 'phone_number')
    ordering = ('-created',)
    inlines = [OrderItemInline]
