from django.contrib import admin
from .models import CartItem
from .models import Order,OrderItem

admin.site.register(CartItem)
# Register your models here.


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','user','address','payment_method','created_at')
    inlines = [OrderItemInline]




# Register your models here.
