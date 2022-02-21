from django.contrib import admin
from .models import Noutbuk


@admin.register(Noutbuk)
class NoutbukAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'brand')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'brand')
    fields = ('id', 'name')
    save_on_top = True
    list_filter = ('price', 'name')
