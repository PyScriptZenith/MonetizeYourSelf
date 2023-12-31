from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from users.forms import UserForm, UserRegisterForm
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogOutView

from users.models import User


class LoginView(BaseLoginView):
    template_name = 'users/login.html'
    success_url = reverse_lazy('monetizeyourself:post_list')

class LogoutView(BaseLogOutView):
    pass

class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('monetizeyourself:post_list')


class UserUpdateView(UpdateView):
    model = User
    success_url = reverse_lazy('users:profile')
    form_class = UserForm
