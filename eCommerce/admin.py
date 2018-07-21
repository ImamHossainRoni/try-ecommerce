from django.contrib import admin
from . models import Category,Product,Brand
# Register your models here.

class CategoryModel(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["__str__",]
    class Meta:
        Model = Category
admin.site.register(Category,CategoryModel)
class BrandModel(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["__str__"]
    class Meta:
        Model = Brand
admin.site.register(Brand,BrandModel)

class ProductModel(admin.ModelAdmin):
    list_display=["__str__"]
    #search_fields = ["__str__"]
    class Meta:
        Model = Product
admin.site.register(Product,ProductModel)