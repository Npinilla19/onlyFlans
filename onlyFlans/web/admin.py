from django.contrib import admin
from .models import Flan


@admin.register(Flan)
class FlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_private', 'flan_uuid')
    search_fields = ('name', 'description')
