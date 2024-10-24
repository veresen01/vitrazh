from django import template
import myapp.views as views
from myapp.models import Category, TagPost
from myapp.utils import menu

register = template.Library()


# @register.simple_tag() # создали простой тег
# def get_categories():
#     return views.cats_db

@register.simple_tag() # создали простой тег
def get_menu():
    return menu


@register.inclusion_tag('myapp/list_categories.html')#включающий тег , в скобках путь к шаблону который будет возвращаться тегом
def show_categories(cat_selected=0): # cat_selected для подсвечивания пунктов меню категории
    # cats=views.cats_db
    cats = Category.objects.all()# Прочитаем все рубрики
    return {'cats': cats, 'cat_selected': cat_selected}

@register.inclusion_tag('myapp/list_tags.html')
def show_all_tags(cat_selected=0): # рии
    # cats=views.cats_db
    cats = Category.objects.all()# Прочитаем все рубрики
    return {'tagd': TagPost.objects.all()}