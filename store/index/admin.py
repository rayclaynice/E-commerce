from django.contrib import admin
from . models import Product, Category

# Register your models here.
#admin.site.register(Product)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)} #the slug will share tthe same value with the name, key = value


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)} # the slug will share the same value with the title key=value


