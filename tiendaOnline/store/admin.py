from django.contrib import admin

from .models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated")

class ProductAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated")

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
