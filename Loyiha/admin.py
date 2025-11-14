from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Main)
class MainAdmin(admin.ModelAdmin):
    list_display = ['rasm', 'tavsif', 'haqida']
    list_filter = ['rasm', 'tavsif', 'haqida']
    search_fields = ['rasm', 'tavsif', 'haqida']
 
    
    
