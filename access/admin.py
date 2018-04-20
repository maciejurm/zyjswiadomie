from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'total', 'status')

admin.site.register(Order, OrderAdmin)

