from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class UserCreateForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    birth_date = forms.DateField()

    class Meta:
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'birth_date')
        model = get_user_model()

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            self.fields['username'].label = 'Display Name'
            self.fields['email'].label = "Email Address"
