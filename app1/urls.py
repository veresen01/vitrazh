from django.urls import path
from . import views
from .views import page_not_found

urlpatterns = [
    path('', views.index, name='index'),
    # path('cats/<slug:cat_slug>/', views.categories, name='cats'),
    path('about/', views.about, name='about'),
    path('galery/', views.galery, name='galery'),
    path('contact/', views.contact, name='contact'),
    path('vitrazh/<slug:vitrazh_slug>/', views.show_vitrazh, name='vitrazh'),
]


handler404=page_not_found