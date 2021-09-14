from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm


class UpdateProfile(forms.ModelForm):
    username = forms.CharField(required=True)
    # email = forms.EmailField(required=True)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    phone = forms.CharField(required=False)
    address = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'phone', 'address')