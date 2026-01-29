from django.contrib import admin
from .models import Product, Category
from .models import Cart, CartItem

admin.site.register(Cart)
admin.site.register(CartItem)



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ("name", "is_active")
    list_filter = ("is_active",)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "price", "is_active")
    list_filter = ("category", "is_active")
    prepopulated_fields = {"slug": ("title",)}
