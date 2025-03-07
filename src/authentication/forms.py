from django import forms
from django.conf import settings

class UserCreateForm(forms.Form):
    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ['username', 'password']