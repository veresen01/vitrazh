python manage.py shell  - открываем оболочку django
from myapp.models import Recipe -импортируем класс Recipe
Recipe(title='Борщ',content='Борщ — горячий заправочный суп на основе свёклы, которая придаёт ему характерный красный цвет.') - создаем экземпляр класса
w1=_  - создаем переменную которая ссылается на последний созданный обьект
w1.save() -сохраняем данные в таблицу

Установить пакет ipython
python manage.py shell
pip install django-extensions
INSTALLED_APPS = (
    ...
    'django_extensions',
    ...
)

[//]: # (python manage.py shell_plus --print-sql - открываем оболочку django с коммандами sql)

Recipe.objects.create(title="Грибной суп", content="ХГрибной суп — суп, основным ингредиентом которого являются грибы.")  -создаем новую запись, сразу в БД
Recipe.objects.all()  выводим кверисет по всем записям в бд
w=Recipe.objects.all()[0]  -прочитали 1ую запись
w=Recipe.objects.all()[:3]  -прочитали первые 3  записи
Recipe.objects.filter(title='Борщ') нашли запись 'Борщ'
Recipe.objects.filter(pk__gte=2) нашли запии где pk>2
Recipe.objects.filter(title__contains='ор') нашли запии где в заголовке есть ор
Recipe.objects.filter(pk__in[2,5,7]) нашли запиcи где где pk=2,5,5
Recipe.objects.exclude(pk=2)  исключает запись с pk=2
Recipe.objects.get(pk=2) возвращает 1 запись- не список
Recipe.objects.all().order_by("title") сортировка по "title"
Recipe.objects.filter(pk__lte=4).order_by("title") сортировка первых 4 записей по title

q=Recipe.objects.get(pk=2) взяли запись pk=2
q.title="Суп" изменили заголовок
q.save() -сохраняем данные в таблицу

Recipe.objects.update(is_published=0) - обновляет у всех записей is_published=0
Recipe.objects.filter(pk__lte=4).update(is_published=1) - обновляет у первых 4 записей is_published=0

q=Recipe.objects.filter(pk__gte=5) ашли запии где pk>5
q.delete() удалили записи


for w in Recipe.objects.all(): 
    w.slug='slug-'+str(w.pk)   для каждой записи заполняем поле slug 'slug-'+str(w.pk)
    w.save()


w.cat_id  -обычное целое число
w.cat  - sql запрос для формирования обьекта класса Category

c=Category.objects.get(pk=1)
c.recipe_set менеджер записи, через него можно выбрать все посты связанные с категорией
c.recipe_set.all()


Recipe.objects.filter(cat__slug="sup") вывод записей по категория=слагу
Recipe.objects.filter(cat__name__contains="ч")  вывод записей где в названии категории есть буква ч

TagPost.objects.create(tag="Холодный",slug="cold")

tag_br=TagPost.objects.all()[1]
tag_o,tag_v =TagPost.objects.filter(id__in[3,5])
a.tags.set([tag_br,tag_o,tag_v])
a.tags.remove(tag_0)
a.tags.add(tag_0)
a.tags.all

Пагинация

recipe=[......]  значения из бд
from.django.core.paginator import Paginator
p=Paginator(recipe,3)  список с которым связан и колво элем на 1 странице
p.count
p.num_pages -кол во страниц
p.page_range итератор
p1=p.page(1) возбмем 1 страницу
p1.object_list список элем 1ой страницы
p1.has_next() возвращает тру если есть след страница
p1.has_pervious() возвращает тру если есть предыд страница



from.django.core.mail import send_mail функция отправки писем в консоль

send_mail(
    "от Юры",
    "Привет.",
    "from@exadmin.ru"],
    ['you@mail.ru'] адреса получателей
    #fail_silently=False,
)

