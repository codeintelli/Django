from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy, gettext as _
from django.contrib.auth import password_validation
from .models import Customer, CancledOrders, ReturnOrders


class CustomerRegistrationForm(UserCreationForm):
    password1 = forms.CharField(required=True, label="Password",
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(required=True, label="Confirm Password",
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.CharField(required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {'email': 'Email'}
        widgets = {'username': forms.TextInput(
            attrs={'class': 'form-control'})}


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(
        attrs={'autofocus': True, 'class': 'form-control'}))
    password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'current-password', 'class': 'form-control mb-5'}))


class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=_('Old Password'), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'current-password', 'autofocus': True, 'class': 'form-control mb-3'}))
    new_password1 = forms.CharField(label=_('New Password'), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'new-password', 'class': 'form-control mb-3'}), help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_('Confirm New Password'), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'new-password', 'class': 'form-control '}))


class MyPasswordResetForm(PasswordResetForm):
    email = forms.CharField(required=True, label=_("Email"), widget=forms.EmailInput(
        attrs={'class': 'form-control', 'autocomplete': 'email'}))


class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label=_('New Password'), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'new-password', 'class': 'form-control mb-3'}), help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_('Confirm New Password'), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'new-password', 'class': 'form-control '}))


class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'locality', 'city', 'state', 'zipcode']
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'}), 'locality': forms.TextInput(attrs={'class': 'form-control'}), 'city': forms.TextInput(
            attrs={'class': 'form-control'}), 'state': forms.Select(attrs={'class': 'form-control'}), 'zipcode': forms.NumberInput(attrs={'class': 'form-control'})}


class CancledOrdersForm(forms.ModelForm):
    class Meta:
        model = CancledOrders
        fields = ['reason', 'bank_name', 'bank_acc',
                  'bank_ifsc', 'holder_name', 'upi_id']
        labels = {'reason': 'Cancle Product Reason', 'bank_name': 'Bank Name', 'bank_acc': 'Bank Account Number',
                  'bank_ifsc': 'Bank IFSC Number', 'holder_name': 'Account Holder Name', 'upi_id': 'Upi Id'}
        widgets = {
            'reason': forms.Select(attrs={'class': 'form-control', 'required': 'true'}),
            'bank_name': forms.Select(attrs={'class': 'form-control', 'required': 'true'}),
            'bank_acc': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
            'bank_ifsc': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
            'holder_name': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
            'upi_id': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
        }


class ReturnOrdersForm(forms.ModelForm):

    class Meta:
        model = ReturnOrders
        fields = ['rreason', 'bank_name', 'bank_acc',
                  'bank_ifsc', 'holder_name', 'upi_id']
        labels = {'rreason': 'Return Product Reason', 'bank_name': 'Bank Name', 'bank_acc': 'Bank Account Number',
                  'bank_ifsc': 'Bank IFSC Number', 'holder_name': 'Account Holder Name', 'upi_id': 'Upi Id'}
        widgets = {
            'rreason': forms.Select(attrs={'class': 'form-control'}),
            'bank_name': forms.Select(attrs={'class': 'form-control'}),
            'bank_acc': forms.TextInput(attrs={'class': 'form-control'}),
            'bank_ifsc': forms.TextInput(attrs={'class': 'form-control'}),
            'holder_name': forms.TextInput(attrs={'class': 'form-control'}),
            'upi_id': forms.TextInput(attrs={'class': 'form-control'}),
        }
