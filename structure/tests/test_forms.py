from django.test import SimpleTestCase, TestCase
from django.db.models import F
from structure.models import Employee, Position

from structure.forms import AddEmployeeForm, SearchEmployeeForm, UpdateEmployeeDetailForm, UserLoginForm


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
            self.form.fields['position_id'].label is None or
            self.form.fields['position_id'].label == 'должность'
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
    """Тест формы добавления нового сотрудника"""

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
    """Тест формы обновления данных сотрудника"""

    fixtures = {'positions.json'}

    def setUp(self):
        self.positions = Position.objects.all()
        self.employee = Employee.objects.create(
            first_name='Николай',
            last_name='Фролов',
            patronymic='Семёнович',
            position=self.positions[17],
            salary=63_000,
        )

    def test_form_field(self):
        # Проверка полей формы
        form = UpdateEmployeeDetailForm(instance=self.employee)
        self.assertEqual(
            list(form.base_fields), [
                'last_name',
                'first_name',
                'patronymic',
                'position',
                'employment_date',
                'salary',
            ]
        )

    def test_form_queryset(self):
        # Проверка доступных для выбора должностей (у которых имеются вакансии)
        form1 = UpdateEmployeeDetailForm(instance=self.employee)
        self.assertEqual(len(form1.fields['position'].queryset), 47)

        Position.objects.filter(id=1).update(vacancies=F('vacancies') - 1)

        form2 = UpdateEmployeeDetailForm(instance=self.employee)
        self.assertEqual(len(form2.fields['position'].queryset), 46)
