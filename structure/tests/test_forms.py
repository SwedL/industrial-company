from django.test import TestCase, SimpleTestCase
from django.urls import reverse
from django.db.models import F
from django.contrib.auth.models import User

from http import HTTPStatus

from structure.forms import *


class UserLoginFormTest(TestCase):
    """Тест формы авторизации пользователя"""

    def setUp(self):
        self.form = UserLoginForm()

    def test_form_field_label(self):
        # Проверка названий полей формы
        self.assertTrue(
            self.form.fields['username'].label is None or self.form.fields['username'].label == 'Логин')
        self.assertTrue(
            self.form.fields['password'].label is None or self.form.fields['password'].label == 'Пароль')

    def test_user_form_validation_for_blank_items(self):
        form = UserLoginForm(data={'username': '', 'password': ''})
        self.assertFalse(form.is_valid())


class SearchEmployeeFormTest(SimpleTestCase):
    """Тест формы поиска и фильтра сотрудников"""

    def setUp(self):
        self.form = SearchEmployeeForm()

    def test_form_field_label(self):
        # Проверка названий полей формы
        self.assertTrue(
            self.form.fields['last_name'].label is None or
            self.form.fields['last_name'].label == 'фамилия'
        )
        self.assertTrue(
            self.form.fields['first_name'].label is None or
            self.form.fields['first_name'].label == 'имя'
        )
        self.assertTrue(
            self.form.fields['patronymic'].label is None or
            self.form.fields['patronymic'].label == 'отчество'
        )
        self.assertTrue(
            self.form.fields['position'].label is None or
            self.form.fields['position'].label == 'должность'
        )
        self.assertTrue(
            self.form.fields['employment_date'].label is None or
            self.form.fields['employment_date'].label == 'дата приёма на работу'
        )
        self.assertTrue(
            self.form.fields['salary'].label is None or
            self.form.fields['salary'].label == 'зарплата'
        )


class AddEmployeeFormTest(TestCase):
    """Тест формы добавления сотрудников"""

    def setUp(self):
        self.form = AddEmployeeForm()

    def test_form_field(self):
        # Проверка полей формы
        self.assertEqual(
            list(self.form.base_fields), [
                'last_name',
                'first_name',
                'patronymic',
                'employment_date',
                'salary',
            ]
        )


class UpdateEmployeeDetailFormTest(TestCase):
    """Тест формы обновления данных сотрудников"""

    fixtures = {'positions.json'}

    def setUp(self):
        self.positions = Position.objects.all()
        self.form = UpdateEmployeeDetailForm()

    def test_form_field(self):
        # Проверка полей формы
        self.assertEqual(
            list(self.form.base_fields), [
                'last_name',
                'first_name',
                'patronymic',
                'position',
                'employment_date',
                'salary',
            ]
        )

    def test_form_queryset(self):
        # Проверка выбора должностей согласно вакансиям, поля position в форме выбора
        form1 = UpdateEmployeeDetailForm()
        self.assertEqual(len(form1.fields['position'].queryset), 47)
        Position.objects.filter(id=1).update(vacancies=F('vacancies') - 1)
        form2 = UpdateEmployeeDetailForm()
        self.assertEqual(len(form2.fields['position'].queryset), 46)
