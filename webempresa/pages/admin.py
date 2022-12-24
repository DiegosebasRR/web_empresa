from django.contrib import admin
from .models import Page
# Register your models here.
class PagesAdmin(admin.ModelAdmin):
    readonly_fields= ('created','updated')
    list_display = ('title','order')
admin.site.register(Page, PagesAdmin)