from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm


# class LoginUserForm(forms.Form):#форма не связанная с моделью- наследуется от Form
class LoginUserForm(AuthenticationForm):#форма не связанная с моделью- наследуется от Form
    username = forms.CharField(label="Логин",
                    widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label="Пароль",
                    widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model =get_user_model()# функция возвращает текущую модель пользователя
        fields=['username','password']



# class RegisterUserForm(forms.ModelForm):#регистрация
#     username = forms.CharField(label="Логин")
#     password = forms.CharField(label="Пароль", widget=forms.PasswordInput())
#     password2 = forms.CharField(label="Повтор пароля", widget=forms.PasswordInput())
#
#     class Meta: #тк форма связана с моделью
#         model = get_user_model()#текущая модель пользователя
#         fields = ['username', 'email', 'first_name', 'last_name', 'password', 'password2']#тполя в форме которые будут отображаться
#         labels = {#метки для полей
#             'email': 'E-mail',
#             'first_name': "Имя",
#             'last_name': "Фамилия",
#         }
#
#     def clean_password2(self):# проверка паролей
#         cd = self.cleaned_data
#         if cd['password'] != cd['password2']:
#             raise forms.ValidationError("Пароли не совпадают!")
#         return cd['password']
#
#     def clean_email(self):# проверка уникальности емэйл
#         email = self.cleaned_data['email']
#         if get_user_model().objects.filter(email=email).exists():
#             raise forms.ValidationError("Такой E-mail уже существует!")
#         return email



class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label="Повтор пароля", widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        labels = {
            'email': 'E-mail',
            'first_name': "Имя",
            'last_name': "Фамилия",
        }
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-input'}),
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'}),
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("Такой E-mail уже существует!")
        return email



class ProfileUserForm(forms.ModelForm): #Профайл пользователя
    username = forms.CharField(disabled=True, label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.CharField(disabled=True, label='E-mail', widget=forms.TextInput(attrs={'class': 'form-input'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name']
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'}),
        }

class UserPasswordChangeForm(PasswordChangeForm):#смена пароля
    old_password = forms.CharField(label="Старый пароль", widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    new_password1 = forms.CharField(label="Новый пароль", widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    new_password2 = forms.CharField(label="Подтверждение пароля", widget=forms.PasswordInput(attrs={'class': 'form-input'}))