from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView, UpdateView

from .forms import AddPostForm, UploadFileForm
from .models import Recipe, Category, TagPost, UploadFiles
from .utils import DataMixin

# menu = ['О сайте', 'Добавить рецепт', 'Обратная связь', 'Войти']


# menu = [{'title': "О сайте", 'url_name': 'about'},
#         {'title': "Добавить статью", 'url_name': 'add_page'},
#         {'title': "Обратная связь", 'url_name': 'contact'},
#         {'title': "Войти", 'url_name': 'login'}
#         ]


# data_db = [
#     {'id': 1, 'title': 'Борщ', 'content': '''<h4>Борщ</h4>, одно из основных блюд в кулинарии, похлёбка из разного рода компонентов, определяющим из которых является свёкла.Широко распространён во многих национальных кухнях, прежде всего, у славян и их ближайших соседей, имея при этом сходные наименования: у русских, украинцев (борщ), белорусов (боршч), литовцев (barščiai «барщчяй»), молдаван (борш, borş), поляков (barszcz «баршч»), румын (borş «борш»).''', 'is_published': True},
#     {'id': 2, 'title': 'Солянка', 'content': 'Рецепт солянки', 'is_published': False},
#     {'id': 3, 'title': 'Щи', 'content': 'Рецепт щей', 'is_published': True},
# ] # имитация базы данных

# cats_db=[
#     {'id':1,'name': 'Супы'},
#     {'id':2,'name': 'Салаты'},
#     {'id':3,'name': 'Горячие блюда'},
# ] # имитация базы данных для пользовательских тегов


# def index(request):  # request -это ссылка на класс HttpRequest
#     posts = Recipe.published.all().select_related('cat') # новый менеджер выводит только опубликованые статьи/ select_related('cat') -жадная загрузка чтобы запрос н едублировался,('cat') атрибут через который связан с табл категорий
#     # posts = Recipe.objects.filter(is_published=1)
#
#     data = {
#         'title': 'Главная страница',
#         'menu': menu,
#         # 'posts': data_db,
#         'posts': posts,
#         'cat_selected':0,
#     }  # передаем словарь в шаблон, вместо title  будет главная страница
#
#     return render(request, "myapp/index.html", context=data)
#     # return HttpResponse("Hello, world!")


# class RecipeHome(ListView):  # замена def index на RecipeHome
#     # model = Recipe  # связка с базой данных
#     template_name = "myapp/index.html"  # определяем шаблон
#     context_object_name = 'posts'  # переменная которая содержит список статей
#     extra_context = {  # для меню верхнего
#         'title': 'Главная страница',
#         'menu': menu,
#         'cat_selected': 0,
#
#     }
#
#     def get_queryset(self):
#         return Recipe.published.all().select_related('cat')

    # extra_context = {# для TemplateView
    #     'title': 'Главная страница',
    #             'menu': menu,
    #             'posts': Recipe.published.all().select_related('cat'),
    #             'cat_selected':0,
    #
    # }


class RecipeHome(DataMixin,ListView):  # замена  на  DataMixin
    template_name = "myapp/index.html"  # определяем шаблон
    context_object_name = 'posts'  # переменная которая содержит список статей
    title_page='Главная страница'
    cat_selected = 0


    def get_queryset(self):
        return Recipe.published.all().select_related('cat')




# def handle_uploaded_file(f):  # функция для загрузки файла по частям
#     with open(f"uploads/{f.name}", "wb+") as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)


# def about(request):  # функция загрузки файла
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             # handle_uploaded_file(form.cleaned_data['file'])
#             fp = UploadFiles(file=form.cleaned_data['file'])
#             fp.save()
#     else:
#         form = UploadFileForm()
#
#     return render(request, "myapp/about.html", {'title': 'о нас',
#                                                 # 'menu': menu,
#                                                 'form': form})


@login_required #страница доступна только для авторизованных
def about(request): #пагинация
    contact_list = Recipe.published.all()
    paginator = Paginator(contact_list, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number) #берем номер текущей отображаемой страницы из гет запроса

    return render(request, 'myapp/about.html',
                  {'title': 'О сайте', 'page_obj': page_obj})

# def show_post(request, post_id):
# def show_post(request, post_slug):
#     post = get_object_or_404(Recipe,
#                              slug=post_slug)  # Из модели Recipe взять запись pk=post_slug, выдает или 1 запись или 404
#     data = {'title': post.title,  # заголовок статьи
#             'menu': menu,
#             'post': post,
#             'cat_selected': 1
#             }
#     return render(request, "myapp/post.html", data)
#     # return HttpResponse(f'Отображение рецепта с id= {post_id}')

# class ShowPost(DetailView):
#     # model = Recipe
#     template_name = 'myapp/post.html'
#     slug_url_kwarg = 'post_slug'# указываем переменную корая будет в марщруте
#     context_object_name = 'post' # указываем переменную корая будет в шаблоне
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = context['post'].title
#         context['menu'] = menu
#         return context
#
#     def get_object(self, queryset=None): # отбираем записи которые опубликованны
#         return get_object_or_404(Recipe.published, slug=self.kwargs[self.slug_url_kwarg])

class ShowPost(DataMixin, DetailView):# вариант с Mixin, DataMixin отвечает за наполнение шаблонов стандартной информацией, чтоб убрать дублирование кода
    template_name = 'myapp/post.html'
    slug_url_kwarg = 'post_slug'# указываем переменную корая будет в марщруте
    context_object_name = 'post' # указываем переменную корая будет в шаблоне

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context,title=context['post'].title)


    def get_object(self, queryset=None): # отбираем записи которые опубликованны
        return get_object_or_404(Recipe.published, slug=self.kwargs[self.slug_url_kwarg])


# def categories(request, cat_id):
#     if cat_id > 15:
#         return redirect("index")  # Перенаправление на страницу ("index")
#     return HttpResponse(f"<h1>Рецепты по категориям</h1><p>id:{cat_id}</p>")
#
#
# def categories_by_slug(request, cat_slug):
#     return HttpResponse(f"<h1>Рецепты по категориям</h1><p>id:{cat_slug}</p>")

# def addpage(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST,request.FILES)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             # try:
#             #     Recipe.objects.create(**form.cleaned_data) # **form.cleaned_data распаковываем словарь для создания новой записи
#             #     return redirect('index')
#             # except:
#             #     form.add_error(None, "Ошибка добавления рецепта")
#             form.save()
#             return redirect('index')
#
#     #если гет запрос то передается пустая форма
#     else:
#         form = AddPostForm()
#     # form=AddPostForm() #создание экземпляра класса из форм
#     data={
#         'menu': menu,
#         'title': 'Добавление статьи',
#         'form': form
#     }
#
#
#     return render(request,"myapp/addpage.html",data)

# class AddPage(FormView):
#     form_class = AddPostForm # ссылается на класс формы
#     template_name = "myapp/addpage.html"
#     success_url = reverse_lazy('index') # reverse_lazy вместо reverse, выстраивает маршрут не сразу а когда он необходим
#     extra_context = {  # для меню верхнего
#         'title': 'Добавление рецепта',
#         'menu': menu,
#     }
#
#     def form_valid(self, form): # сохранение в бд,вызывается после проверки полей формы
#         form.save()
#         return super().form_valid(form)

# class AddPage(CreateView):
#     form_class = AddPostForm # ссылается на класс формы
#     # model = Recipe
#     # fields = '__all__'#указать поля которые будут отражены в форме
#     template_name = "myapp/addpage.html"
#     success_url = reverse_lazy('index') # reverse_lazy вместо reverse, выстраивает маршрут не сразу а когда он необходим
#     extra_context = {  # для меню верхнего
#         'title': 'Добавление рецепта',
#         'menu': menu,
#     }

class AddPage(LoginRequiredMixin,DataMixin,CreateView):
    form_class = AddPostForm # ссылается на класс формы
    template_name = "myapp/addpage.html"
    title_page = 'Добавление рецепта'

    def form_valid(self, form): #провернееная и заполненная форма добавления рецепта
        w=form.save(commit=False) #обьект новой записи для бд, но пока не записываем
        w.author=self.request.user #связка автора и текущего пользоавтеля
        return  super().form_valid(form) #сохраняем в бд


# class UpdatePage(UpdateView): #Редактирование
#     model = Recipe
#     fields = ['title','content','photo','is_published','cat']#указать поля которые будут отражены в форме
#     template_name = "myapp/addpage.html"
#     success_url = reverse_lazy('index') # reverse_lazy вместо reverse, выстраивает маршрут не сразу а когда он необходим
#     extra_context = {  # для меню верхнего
#         'title': 'Редактирование рецепта',
#         'menu': menu,
#     }


class UpdatePage(DataMixin,UpdateView): #Редактирование
    model = Recipe
    fields = ['title','content','photo','is_published','cat']#указать поля которые будут отражены в форме
    template_name = "myapp/addpage.html"
    success_url = reverse_lazy('index') # reverse_lazy вместо reverse, выстраивает маршрут не сразу а когда он необходим
    title_page ='Редактирование рецепта'




# class AddPage(View):  # класс AddPage, вместо def addpage
#     def get(self, request):
#         form = AddPostForm()
#         data = {
#             'menu': menu,
#             'title': 'Добавление статьи',
#             'form': form
#         }
#         return render(request, "myapp/addpage.html", data)
#
#     def post(self, request):
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#
#         data = {
#             'menu': menu,
#             'title': 'Добавление статьи',
#             'form': form
#         }
#         return render(request, "myapp/addpage.html", data)


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


# def show_category(request, cat_slug):
#     category = get_object_or_404(Category, slug=cat_slug)  # slug=cat_slug критерий по которому будет отбираться запись
#     posts = Recipe.published.filter(cat_id=category.pk).select_related(
#         'cat')  # отбираются статьи у которых cat_id=categoryюзл
#     data = {
#         # 'title': 'Главная страница',
#         # 'menu': menu,
#         # 'posts': data_db,
#         # 'cat_selected': cat_id,
#         'title': f'Рубрика:{category.name}',
#         'menu': menu,
#         'posts': posts,
#         'cat_selected': category.pk,
#     }  # передаем словарь в шаблон, вместо title  будет главная страница
#
#     return render(request, "myapp/index.html", context=data)

# class RecipeCategory(ListView):
#     template_name = 'myapp/index.html'
#     context_object_name = 'posts'
#     allow_empty = False  # ошибка 404
#
#     def get_queryset(self):
#         return Recipe.published.filter(cat__slug=self.kwargs['cat_slug']).select_related(
#             'cat')  # отбираются статьи у которых cat_id=categoryюзл
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         cat = context['posts'][0].cat
#         context['title'] = 'Категория - ' + cat.name
#         context['menu'] = menu
#         context['cat_selected'] = cat.pk
#         return context


class RecipeCategory(DataMixin,ListView):
    template_name = 'myapp/index.html'
    context_object_name = 'posts'
    allow_empty = False  # ошибка 404


    def get_queryset(self):
        return Recipe.published.filter(cat__slug=self.kwargs['cat_slug']).select_related(
            'cat')  # отбираются статьи у которых cat_id=categoryюзл

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cat = context['posts'][0].cat
        return self.get_mixin_context(context,
                                      title='Категория - ' + cat.name,
                                      cat_selected=cat.pk,
                                      )


# def show_tag_postlist(request, tag_slug):
#     tag = get_object_or_404(TagPost, slug=tag_slug)
#     posts = tag.tags.filter(is_published=Women.Status.PUBLISHED).select_related("cat")
#
#     data = {
#         'title': f"Тег: {tag.tag}",
#         'menu': menu,
#         'posts': posts,
#         'cat_selected': None,
#     }
#
#     return render(request, 'women/index.html', context=data)


# class TagPostList(ListView):
#     template_name = 'women/index.html'
#     context_object_name = 'posts'
#     allow_empty = False
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         tag = TagPost.objects.get(slug=self.kwargs['tag_slug'])
#         context['title'] = 'Тег: ' + tag.tag
#         context['menu'] = menu
#         context['cat_selected'] = None
#         return context
#
#     def get_queryset(self):
#         return Recipe.published.filter(tags__slug=self.kwargs['tag_slug']).select_related('cat')


class TagPostList(DataMixin, ListView):
    template_name = 'recipe/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = TagPost.objects.get(slug=self.kwargs['tag_slug'])
        return self.get_mixin_context(context, title='Тег: ' + tag.tag)

    def get_queryset(self):
        return Recipe.published.filter(tags__slug=self.kwargs['tag_slug']).select_related('cat')

# функция представление для несуществующих страниц.работает при Debug=True
def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
