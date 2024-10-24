from django.urls import path
from . import views
from .views import page_not_found

urlpatterns = [
 # path('', views.index, name='index'),
 path('', views.RecipeHome.as_view(), name='index'),
 path('about/', views.about, name='about'),
 # path('addpage/', views.addpage, name='add_page'),
 path('addpage/', views.AddPage.as_view(), name='add_page'),
 path('contact/', views.contact, name='contact'),
 path('login/', views.login, name='login'),
 # path('post/<int:post_id>/', views.show_post, name='post'), # пост отоброжается по айди
 # path('post/<slug:post_slug>/', views.show_post, name='post'), # пост отоброжается по slug
 path('post/<slug:post_slug>/', views.ShowPost.as_view(), name='post'), # пост отоброжается по slug
 # path('category/<slug:cat_slug>/', views.show_category, name='category'), #адреса для категорий
 path('category/<slug:cat_slug>/', views.RecipeCategory.as_view(), name='category'), #адреса для категорий
 # path('tag/<slug:tag_slug>/', views.show_tag_postlist, name='tag'), #отображаем статьи связанные с тегом
 path('tag/<slug:tag_slug>/', views.TagPostList.as_view(), name='tag'), #отображаем статьи связанные с тегом
 # path('cats/<int:cat_id>/', views.categories, name='categories'),
 # path('cats/<slug:cat_slug>/', views.categories_by_slug, name='categories_by_slug'),
 path('edit/<slug:slug>/', views.UpdatePage.as_view(), name='edit_page'), #редактируем статью по slug

]

handler404=page_not_found # обработчик 404, фнкция page_not_found во views. работает при Debug=True