from django.contrib import admin
from .form import StockCreateForm

from .models import Stock
# Register your models here.



class StockCreateAdmin(admin.ModelAdmin):
    list_display = ['category','item_name','quantity']
    form = StockCreateForm
    list_filter = ['category']
    search_fields = ['category','item_name']


admin.site.register(Stock,StockCreateAdmin)


