from django.contrib import admin
from .models import Order
from django.utils.html import format_html

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('status', 'id', 'model', 'user', 'created_at', 'price')
    list_filter = ('status',)
    search_fields = ('user__user',)
    ordering = ('-created_at',)

    def model_display(self, obj):
        return obj.model
    model_display.short_description = 'Модел'
    
