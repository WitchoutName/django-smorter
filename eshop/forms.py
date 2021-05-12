from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput
from django.utils.translation import ugettext_lazy as _
from .models import *


class RegisterForm(UserCreationForm):
    username = forms.RegexField(
        label=_(""), max_length=30, regex=r"^[\w.@+-]+$",
        error_messages={
            'invalid': _("This value may contain only letters, numbers and "
                         "@/./+/-/_ characters.")},
        widget=TextInput(attrs={'class': 'form-control mb-3',
                                'required': 'true',
                                'placeholder': 'Username'
                                })
    )

    password1 = forms.CharField(
        label=_(""),
        widget=forms.PasswordInput(attrs={'class': 'form-control mb-3',
                                          'required': 'true',
                                          'type': 'password',
                                          'placeholder': 'Password'
                                          })
    )
    password2 = forms.CharField(
        label=_(""),
        widget=forms.PasswordInput(attrs={'class': 'form-control mb-3',
                                          'type': 'password',
                                          'required': 'true',
                                          'placeholder': 'Password again'
                                          }),
    )


    email = forms.CharField(
        label=_(''),
        widget=forms.TextInput(attrs={'class': 'form-control mb-3',
                                      'type': 'email',
                                      'placeholder': 'Email',
                                      'required': 'true'
                                      })
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class ShopCreateForm(forms.ModelForm):
    admins = forms.CharField(label=_(''), widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))

    class Meta:
        model = Shop
        fields = ["owner", "title", "description", "payment_methods", "shipment_methods", "image", "admin_group", "admins"]
        labels = {x:"" for x in fields}
        labels["payment_methods"] = "Select your payment methods"
        labels["shipment_methods"] = "Select your shipment methods"
        labels["image"] = "Upload your banner"
        widgets = {
            "title": forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Shop title', 'required': 'true'}),
            "description": forms.Textarea(attrs={'class': 'form-control mb-3', 'placeholder': 'Shop Description'}),
            "payment_methods": forms.SelectMultiple(attrs={'class': 'form-select mb-3'}),
            "shipment_methods": forms.SelectMultiple(attrs={'class': 'form-select mb-3'}),
            "image": forms.FileInput(attrs={'class': 'form-control mb-3', "type": "file"}),
        }