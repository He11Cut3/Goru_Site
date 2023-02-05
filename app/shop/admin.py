from django.contrib import admin
from . import models
from shop.models import Product, Payment, OrderItem, Order, Category, ContactModel
from mptt.admin import MPTTModelAdmin


@admin.register(models.Product)
class PostAdmin(admin.ModelAdmin):
    list_display = ["name","code", "price", "unit", "image", "specifications", "text", "category"]
    save_as = True
    save_on_top = True


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'create_at', 'id']



@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display=["id","name","email","create_at"]
    list_display_links = ["name"]



admin.site.register(Payment)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(models.Category, MPTTModelAdmin)