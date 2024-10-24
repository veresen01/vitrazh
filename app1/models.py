from random import randint

from django.db import models
from django.urls import reverse


class Vitrazh(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(max_length=255, verbose_name="Описание")
    image = models.ImageField(upload_to='photos/', verbose_name="Изображение")
    # slug = models.SlugField(max_length=255, blank=True, db_index=True, default='')
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('vitrazh', kwargs={'vitrazh_slug': self.slug})

    class Meta:
        verbose_name = 'Витражи'
        verbose_name_plural = 'Витражи'




class Master(models.Model):
    fio = models.CharField(max_length=100, verbose_name="ФИО")
    biography = models.TextField(verbose_name="О себе")
    photo = models.ImageField(upload_to='photos/', verbose_name="Фото")

    def __str__(self):
        return self.fio

    class Meta:
        verbose_name = 'Мастер'
        verbose_name_plural = 'Мастер'


class Contact(models.Model):
    adress = models.TextField(verbose_name="Адрес")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    email = models.EmailField(max_length=100, verbose_name="Email")

    def __str__(self):
        return self.adress

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'


class IndexPage(models.Model):
    title = models.TextField(verbose_name="Заголовок")
    one = models.TextField(verbose_name="Первый абзац")
    two = models.TextField(verbose_name="Второй абзац")
    three = models.TextField(verbose_name="Третий абзац")
    four = models.TextField(verbose_name="Четвертый абзац")
    five = models.TextField(verbose_name="Пятый абзац")
    six = models.TextField(verbose_name="Шестой абзац")
    seven = models.TextField(verbose_name="Седьмой абзац")
    eight = models.TextField(verbose_name="Восьмой абзац")
    nine = models.TextField(verbose_name="Девятый абзац")
    ten = models.TextField(verbose_name="Десятый абзац")


    def __str__(self):
        return 'Главная страница'

    class Meta:
        verbose_name = 'Главная'
        verbose_name_plural = 'Главная'
