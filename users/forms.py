from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from monetizeyourself.forms import StyleMixin
from users.models import User


class UserRegisterForm(StyleMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ("phone", "email", "password1", "password2")


class UserForm(StyleMixin, UserChangeForm):
    class Meta:
        model = User
        fields = (
            "email",
            "password",
            "first_name",
            "last_name",
            "phone",
            "city",
            "nick_name",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["password"].widget = forms.HiddenInput()
