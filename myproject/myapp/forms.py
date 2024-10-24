

from django import forms
from .models import Category, Recipe


# class AddPostForm(forms.Form):
#     title = forms.CharField(max_length=255, label="Заголовок", widget=forms.TextInput(attrs={'class': 'form-input'}))
#     slug = forms.SlugField(max_length=255, label="URL")
#     content = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 5}), required=False, label="Контент")  #required=False необяхательный пункт в флрорме
#     is_published = forms.BooleanField(required=False, initial=True, label="Статус")# initial=True стоит галочка
#     cat = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Категория не выбрана", label="Категории")# отображение в виде выпадающего списка


class AddPostForm(forms.ModelForm):

    is_published = forms.BooleanField(required=False, initial=True, label="Статус")# initial=True стоит галочка
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Категория не выбрана", label="Категории")# отображение в виде выпадающего списка


    class Meta: # описывает взаимосвязь формы с Recipe
        model=Recipe
        # fields="__all__"  #те поля которые будут отоброжаться в форме
        fields=['title','slug','photo','content','is_published','cat']
        widgets={
            'title':forms.TextInput(attrs={'class': 'form-input'}),
            'content':forms.Textarea(attrs={'cols': 50, 'rows': 5}),
        }
        labels={'slug':'URL',
               'content':'Рецепт',
               }


class UploadFileForm(forms.Form): # для загрузки файлов
    file = forms.ImageField(label="Файл")
