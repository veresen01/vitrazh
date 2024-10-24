from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Vitrazh, Master, Contact, IndexPage

# Register your models here.

admin.site.site_header = "Панель администрирования"
admin.site.index_title = "Витражи"


@admin.register(Vitrazh)
class VitrazhAdmin(admin.ModelAdmin):
    fields = ['name', 'image', 'vitrazh_photo', 'slug']
    list_display = ('id', 'name', 'vitrazh_photo', 'slug')
    list_display_links = ('id', 'name')
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ['vitrazh_photo']

    @admin.display(description='Витраж', ordering='content')
    def vitrazh_photo(self, vitrazh: Vitrazh):  # отображение фото в админке
        if vitrazh.image:
            return mark_safe(f"<img src='{vitrazh.image.url}' width=50>")
        return 'Без фото'


@admin.register(Master)
class MasterAdmin(admin.ModelAdmin):
    fields = ['fio', 'biography', 'photo']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    fields = ['adress', 'phone', 'email']


@admin.register(IndexPage)
class IndexPageAdmin(admin.ModelAdmin):
    fields = ['title','one', 'two', 'three','four', 'five','six','seven', 'eight', 'nine', 'ten']
