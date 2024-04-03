import json

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q

from ic.settings import BASE_DIR
from structure.models import Employee, Position


class UserLoginForm(AuthenticationForm):
    """ Форма авторизация пользователя """

    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Username'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Password'}))

    class Meta:
        fields = ('username', 'password')


class SearchEmployeeForm(forms.Form):
    """ Форма поиска или фильтрации сотрудников по полям формы """

    DEPARTMENT_CHOICES = [(None, '---')]

    # формируем список поля выбора из фикстуры всех должностей компании
    with open(f'{BASE_DIR}/structure/fixtures/positions.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        for num, i in enumerate(data, 1):
            DEPARTMENT_CHOICES.append((num, i['fields']['name']))

    last_name = forms.CharField(max_length=50, required=False, label='фамилия')
    first_name = forms.CharField(max_length=50, required=False, label='имя',
                                 widget=forms.TextInput(attrs={'id': 'search-input'}))
    patronymic = forms.CharField(max_length=50, required=False, label='отчество')
    position_id = forms.ChoiceField(choices=DEPARTMENT_CHOICES, required=False, label='должность')
    employment_date = forms.DateField(required=False, label='дата приёма на работу',
                                      widget=forms.TextInput(attrs={'placeholder': 'гггг-мм-дд'}))
    salary = forms.IntegerField(required=False, label='зарплата')


class AddEmployeeForm(forms.ModelForm):
    """ Форма добавления нового сотрудника """

    class Meta:
        model = Employee
        fields = ['last_name', 'first_name', 'patronymic', 'employment_date', 'salary']


class UpdateEmployeeDetailForm(forms.ModelForm):
    """ Форма обновления данных сотрудника (поля должность и зарплата) """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # оставляем в queryset только должности с вакансиями и текущую должность сотрудника
        self.fields['position'].queryset = Position.objects.filter(
            Q(vacancies__gt=0) | Q(pk=kwargs['instance'].position_id)
        )

    class Meta:
        model = Employee
        fields = ['last_name', 'first_name', 'patronymic', 'position', 'employment_date', 'salary']

        widgets = {
            'last_name': forms.TextInput(attrs={'class': 'readonly', 'readonly': 'True'}),
            'first_name': forms.TextInput(attrs={'class': 'readonly', 'readonly': 'True'}),
            'patronymic': forms.TextInput(attrs={'class': 'readonly', 'readonly': 'True'}),
            'employment_date': forms.TextInput(attrs={'class': 'readonly', 'readonly': 'True'}),
        }
