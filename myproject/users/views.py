from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView

from .forms import LoginUserForm, RegisterUserForm, ProfileUserForm, UserPasswordChangeForm


class LoginUser(LoginView):
#     form_class = AuthenticationForm
    form_class = LoginUserForm #наследуемся от своего класса
    template_name = 'users/login.html'
    extra_context = {'title': 'Авторизация'}

    # def get_success_url(self):
    #    return reverse_lazy('index')#перенаправление при успешной регистрации


# def login_user(request):
#     if request.method == 'POST': #если метод post
#         form = LoginUserForm(request.POST)# создаем обьект с заполненными данными, из request возьмем коллекцию POST
#         if form.is_valid():# проверка валидации
#             cd = form.cleaned_data
#             user = authenticate(request, username=cd['username'], #аутентификация по бд
#                                 password=cd['password'])
#             if user and user.is_active:
#                 login(request, user) #авторизация
#                 return HttpResponseRedirect(reverse('index')) #перенаправление на главную
#     else:
#         form = LoginUserForm()
#
#     return render(request, 'users/login.html', {'form': form})


def logout_user(request): #выход из с истемы
    logout(request)
    return HttpResponseRedirect(reverse('users:login'))# нужно указать пространство имен



# def register(request):
#     if request.method == 'POST':
#         form = RegisterUserForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.set_password(form.cleaned_data['password']) #шифрование пароля и занесение в атрибут password
#             user.save()
#             return render(request, 'users/register_done.html')
#     else:
#         form = RegisterUserForm()
#     return render(request, 'users/register.html', {'form': form})

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    extra_context = {'title': "Регистрация"}
    success_url = reverse_lazy('users:login')



class ProfileUser(LoginRequiredMixin, UpdateView): #Профайл пользователя
    model = get_user_model()
    form_class = ProfileUserForm
    template_name = 'users/profile.html'
    extra_context = {'title': "Профиль пользователя"}

    def get_success_url(self):
        return reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user

class UserPasswordChange(PasswordChangeView):#смена пароля
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy("users:password_change_done")
    template_name = "users/password_change_form.html"