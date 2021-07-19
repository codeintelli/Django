from django.contrib import admin
from .models import (Customer, Product, Cart, OrderPlaced,
                     ReturnOrders, CancledOrders)
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name',
                    'locality', 'city', 'zipcode', 'state']


@admin.register(Product)
class ProductModelAdmin(SummernoteModelAdmin):
    list_display = ['id', 'title', 'selling_price', 'discount_price',
                    'description', 'brand', 'category', 'product_image']
    summernote_fields = ('description',)


@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'quantity']


@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'customer',
                    'product', 'quantity', 'ordered_date', 'status']


@admin.register(ReturnOrders)
class ReturnOrdersModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'orderplaced',
                    'rreason', 'return_date', 'bank_name', 'bank_acc', 'bank_ifsc', 'holder_name', 'upi_id']


@admin.register(CancledOrders)
class CancledOrdersModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'orderplaced',
                    'reason', 'cancle_date', 'bank_name', 'bank_acc', 'bank_ifsc', 'holder_name', 'upi_id']
