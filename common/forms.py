from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    phone = forms.CharField(label='전화번호', max_length=20, help_text='전화번호 ex)010-1111-2222')
    email = forms.EmailField(label='이메일')

    class Meta:
        model = User
        fields = ("username", 'password1', 'password2', 'phone', 'email')