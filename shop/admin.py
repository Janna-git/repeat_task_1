from django.contrib import admin

from .models import Item, Purchase


class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']


admin.site.register(Item, ItemAdmin)


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'item', 'date_purchase']


admin.site.register(Purchase, PurchaseAdmin)
