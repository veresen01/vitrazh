from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify

def translit_to_eng(s: str) -> str:# функция преобразования руссих букв в латинские, для слага
    d = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd',
         'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i', 'к': 'k',
         'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
         'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch',
         'ш': 'sh', 'щ': 'shch', 'ь': '', 'ы': 'y', 'ъ': '', 'э': 'r', 'ю': 'yu', 'я': 'ya'}

    return "".join(map(lambda x: d[x] if d.get(x, False) else x, s.lower()))





class PublishedManager(models.Manager):#Создание пользовательского менеджера модели, возвращает только опубликованные посты
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Recipe.Status.PUBLISHED)



class Recipe(models.Model):
    class Status(models.IntegerChoices):# для осмысленных имен вместо 1 в PublishedManager
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'

    title=models.CharField(max_length=255,verbose_name='Заголовок') #текстовое поле , макс длинна 255, verbose_name='Заголовок'-заголовок в админке
    slug=models.SlugField(max_length=255,   unique=True, db_index=True) #создаем пол слаг, уникальный, индексируемое поле
    # slug=models.SlugField(max_length=255,   blank=True, db_index=True, default='') #хитрость для миграции,не уникальное, по умолчанию пустая строка
    photo=models.ImageField(upload_to='photos/%Y/%m/%d',default=None,blank=True,null=True,verbose_name='Фото')# поле для загрузки фото
    content=models.TextField(blank=True) #текстовое поле , blank=True -можно ничего не передавать
    time_create=models.DateTimeField(auto_now_add=True)#автоматом создает дату создания записи
    time_update=models.DateTimeField(auto_now=True)#автоматом создает дату обновления записи
    # is_published=models.BooleanField(default=True) #по умолчанию рецепт опубликован
    # is_published = models.BooleanField(choices=Status.choices, default=Status.DRAFT)
    is_published = models.BooleanField(choices=tuple(map(lambda  x:(bool(x[0]),x[1]),Status.choices)), default=Status.DRAFT)#преобразуем 0 и 1 в булевы значения
    # cat=models.ForeignKey('Category', on_delete=models.PROTECT, null=True)#связь многие к одному. models.PROTECT -запрещает удаление категории связанной с постами
    # cat=models.ForeignKey('Category', on_delete=models.PROTECT)#связь многие к одному. models.PROTECT -запрещает удаление категории связанной с постами
    cat=models.ForeignKey('Category', on_delete=models.PROTECT,related_name='posts')#связь многие к одному. models.PROTECT -запрещает удаление категории связанной с постами,related_name='posts'-мен
    tags=models.ManyToManyField('TagPost', blank=True,related_name='tags') # связь многие ко многим Tagpost, related_name='tags'-чтоб через теги получать список статей которые с ними связанны
    author=models.ForeignKey(get_user_model(),on_delete=models.SET_NULL,related_name='posts',null=True,default=None)# связь рецепта и автора

    objects = models.Manager()#сохранили старый менеджер
    published = PublishedManager()#добавили новый менеджер

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Рецепты блюд'# настойка админки
        verbose_name_plural='Рецепты блюд'# настойка админки
        ordering=['-time_create'] # можно прописать сортировку по time_create
        indexes=[  #индексация полей, чтоб сортировка быстрее была
            models.Index(fields=['-time_create'])
        ]



    def get_absolute_url(self):#формируем url адрес для каждой записи
        return reverse('post', kwargs={'post_slug': self.slug})#ИМЯ МАРШРУТА post,


    # def save(self,*args,**kwargs): #формирование слага на основе заголовка
    #     self.slug=slugify(translit_to_eng(self.title))
    #     super().save(*args,**kwargs)


class Category(models.Model):
    name=models.CharField(max_length=100,db_index=True)
    slug=models.SlugField(max_length=255,unique=True, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):#формируем url адрес для каждой записи
        return reverse('category', kwargs={'cat_slug': self.slug})#ИМЯ МАРШРУТА post,

    class Meta:
        verbose_name='Категории'# настойка админки
        verbose_name_plural='Категории'# настойка админки


class TagPost(models.Model):
    tag=models.CharField(max_length=100,db_index=True)
    slug=models.SlugField(max_length=255,unique=True,db_index=True)

    def __str__(self):
        return self.tag

    def get_absolute_url(self):#формируем url адрес для каждой записи
        return reverse('tag', kwargs={'tag_slug': self.slug})#ИМЯ МАРШРУТА ,


class UploadFiles(models.Model): # для загрузки файлов
    file=models.FileField(upload_to='uploads_model') # upload_to='uploads_model' каталог куда будут загружаться файлы