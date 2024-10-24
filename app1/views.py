from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
import random
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify

from app1.models import Vitrazh, Master, Contact,IndexPage

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Галерея', 'url_name': 'galery'},
    {'title': 'Контакты', 'url_name': 'contact'},
]

data_db = [
    {'id': 1, 'name': 'витраж-1', 'description': ' описание витраж-1', 'image': ' картинка витраж-1'},
    {'id': 2, 'name': 'витраж-2', 'description': 'описание витраж-2', 'image': 'картинка витраж-2'},
    {'id': 3, 'name': 'витраж-3', 'description': 'описание витраж-3', 'image': 'картинка витраж-3'},
]


def index(request):
    count = Vitrazh.objects.count()
    randomm = Vitrazh.objects.all()[random.randint(0, count - 1)]



    indexx = IndexPage.objects.filter()[0]

    data = {
        'title': 'Главная страница',
        'indexx': indexx,
        'randomm': randomm,

    }
    return render(request, "app1/index.html", context=data)


def about(request):
    master = Master.objects.filter()[0]
    # about=Master.objects.filter()[1:]

    data = {
        'title': 'О нас',
        'master': master,
        # 'about': about,

    }
    return render(request, "app1/about.html", context=data)


# def categories(request, cat_slug):
#     return HttpResponse(f"<h1>Статьи по категориям</h1><p >slug:{ cat_slug }</p>")


def galery(request):
    vitrazh_1 = Vitrazh.objects.filter()[:3]
    vitrazh_2 = Vitrazh.objects.filter()[4:7]
    vitrazh_3 = Vitrazh.objects.filter()[8:11]

    data = {
        'title': 'ГГалерея',
        'menu': 'ГГалерея витражей',
        'vitrazh_1': vitrazh_1,
        'vitrazh_2': vitrazh_2,
        'vitrazh_3': vitrazh_3,

    }
    return render(request, "app1/galery.html", context=data)


def contact(request):
    contact = Contact.objects.filter()[0]
    master = Master.objects.filter()[0]

    data = {
        'title': 'ККонтакты',
        'menu': 'ННаши контакты',
        'contact': contact,
        'master': master,

    }
    return render(request, "app1/contact.html", context=data)


def show_vitrazh(request, vitrazh_slug):
    vitrazh = get_object_or_404(Vitrazh, slug=vitrazh_slug)

    data = {
        'name': vitrazh.name,
        # 'menu': menu,
        'vitrazh': vitrazh,
        # 'cat_selected': 1,
    }

    return render(request, 'app1/vitrazh.html', context=data)


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
