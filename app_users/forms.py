from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import password_validation

from .models import Profile


class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(
        label=_("*Parol"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("*Parolni tasdiqlang"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text=_("Tekshirish uchun avvalgidek parolni kiriting."),
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']
        labels = {
            'username': '*Nickname',
            'first_name': 'Ismingiz',
            'last_name': 'Familiya',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control',
                'placeholder': f'{field.label}'
            })


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control',
            })