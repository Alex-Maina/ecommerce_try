from django.contrib import admin

# Register your models here.
from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Product)
#modify the products-admin page
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ['title']
    }
    autocomplete_fields =['collection']
    list_display = ['title', 'price','inventory_status', 'collection']
    list_editable = ['price', 'collection']
    ordering =['title']
    search_fields = ['title__istartswith']
    list_filter = ['collection']
    
    @admin.display(ordering='inventory')
    def inventory_status(self,product):
        if product.inventory < 10:
            return 'LOW'
        return 'OK'


@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    search_fields=['title']

admin.site.register(models.Promotion)

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']


admin.site.register(models.Address)
admin.site.register(models.Order)
admin.site.register(models.OrderItem)
admin.site.register(models.Cart)
admin.site.register(models.CartItem)