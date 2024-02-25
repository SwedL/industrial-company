from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse
from django.utils import timezone

from .models import Employee, Position


class UserLoginForm(AuthenticationForm):
    """Форма авторизация пользователя"""

    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Username'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Password'}))

    class Meta:
        fields = ('username', 'password')


class SearchEmployeeForm(forms.Form):
    DEPARTMENT_CHOICES = [(None, '---')] + [(num, p.name) for num, p in enumerate(Position.objects.all(), 1)]

    last_name = forms.CharField(max_length=50, required=False)
    first_name = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'id': 'search-input'}))
    patronymic = forms.CharField(max_length=50, required=False)
    position = forms.ChoiceField(choices=DEPARTMENT_CHOICES, required=False)
    employment_date = forms.DateField(required=False, widget=forms.TextInput(attrs={'placeholder': 'гггг-мм-дд'}))
    salary = forms.IntegerField(required=False)


class AddEmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ['last_name', 'first_name', 'patronymic', 'position', 'employment_date', 'salary']


class UpdateEmployeeDetailForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ['last_name', 'first_name', 'patronymic', 'position', 'employment_date', 'salary']

        widgets = {
            'last_name': forms.TextInput(attrs={'class': 'readonly', 'readonly': 'True'}),
            'first_name': forms.TextInput(attrs={'class': 'readonly', 'readonly': 'True'}),
            'patronymic': forms.TextInput(attrs={'class': 'readonly', 'readonly': 'True'}),
            'employment_date': forms.TextInput(attrs={'class': 'readonly', 'readonly': 'True'}),
        }
