from django.apps import AppConfig


class MyappConfig(AppConfig):
    verbose_name = 'Рецепты блюд'  # настойка админки
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'
