from django.forms import CharField, ModelForm, TextInput, PasswordInput, ChoiceField
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse
from .models import Employee


class UserLoginForm(AuthenticationForm):
    """Форма авторизация пользователя"""

    username = CharField(label='Логин', widget=TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Username'}))
    password = CharField(label='Пароль', widget=PasswordInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Password'}))

    class Meta:
        fields = ('username', 'password')


class AddEmployeeForm(ModelForm):
    # first_name = CharField(required=True, widget=TextInput(attrs={"class": "clrtxt", "placeholder": "Имя"}))
    # last_name = CharField(required=True, widget=TextInput(attrs={"class": "clrtxt", "placeholder": "Фамилия"}))
    # patronymic = CharField(required=True, widget=TextInput(attrs={"class": "clrtxt", "placeholder": "Отчество"}))
    # position = ChoiceField()

    class Meta:
        model = Employee
        fields = ['last_name', 'first_name', 'patronymic', 'employment_date', 'salary']


