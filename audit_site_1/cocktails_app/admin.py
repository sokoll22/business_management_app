from django.contrib import admin

from .models import Cocktail, Category

# Register your models here.


class CocktailAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',  'category', 'is_active', 'bar_price', 'employee_price', 'club_price', 'customer_price')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'bar_price', 'employee_price', 'club_price', 'customer_price')
    list_editable = ('is_active',)
    list_filter = ('category', 'is_active')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(Cocktail, CocktailAdmin)
admin.site.register(Category, CategoryAdmin)

