from django.contrib import admin,messages
from django.utils.safestring import mark_safe

from .models import Recipe, Category


@admin.register(Recipe)#используем admin.site.register(Recipe,RecipeAdmin) как декоратор
class RecipeAdmin(admin.ModelAdmin):
    fields = ['title','content','slug','photo','post_photo','cat'] # выбор полей для редактирования
    # exclude = ['tags','is_published']# исключение полей для редактирования
    readonly_fields =['post_photo'] #отображение полей только для чтения
    prepopulated_fields = {"slug": ("title",)} # формирование слага на основе списка полей
    # list_display = ('id','title','time_create', 'is_published', 'cat') # Оторожение полей в админке
    list_display = ('id','title','post_photo','time_create', 'is_published', 'cat') # Оторожение полей в админке. 'brief_info' убрали
    list_display_links = ('id','title') # кликабельность полей в админке
    ordering =['time_create','title'] # поля сортировки в админке
    list_editable = ('is_published', )# поля редактируемые
    list_per_page = 10 # количество рецептов отображаемых в админке на странице
    actions =['set_published','set_draft'] # добавление set_published. set_draft
    search_fields = ['title__startswith','cat__name']#панель поиска по полю  'title', cat  поле 'cat__name' по люкапу
    list_filter = ['cat__name', 'is_published'] #фильтр
    save_on_top = True# поле сохранить вверху


    # @admin.display(description='краткое опсание', ordering='content')
    # def brief_info(self,recipe: Recipe): #создание пользовательского поля в админке
    #     return f'Описание {len(recipe.content)} символов'

    @admin.display(description='Изображение', ordering='content')
    def post_photo(self,recipe: Recipe): #отображение фото в админке
        if recipe.photo:
            return mark_safe(f"<img src='{recipe.photo.url}' width=50>")
        return "Без фото"


    @admin.action(description='Опубликовать выбранные записи')
    def set_published(self,request,queryset):# добавлеение в выпадающее меню пункта опубликовать записи
        count=queryset.update(is_published=Recipe.Status.PUBLISHED)
        self.message_user(request,f'Изменено {count} записей')#оповещение ждля пользователя

    @admin.action(description='Снять с публикации выбранные записи')
    def set_draft(self, request, queryset):  # добавлеение в выпадающее меню пункта Снятать записи
        count = queryset.update(is_published=Recipe.Status.DRAFT)
        self.message_user(request, f'Снято с публикации {count} записей',messages.WARNING)  # оповещение ждля пользователя

# admin.site.register(Recipe,RecipeAdmin) # регистрация приложения и регистрация RecipeAdmin


@admin.register(Category)#используем admin.site.register(Recipe,RecipeAdmin) как декоратор
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name') # Оторожение полей в админке
    list_display_links = ('id','name') # кликабельность полей в админке
