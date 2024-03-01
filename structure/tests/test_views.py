from django.test import SimpleTestCase, TestCase
from django.contrib.auth.models import User, Permission
from django.urls import reverse

from http import HTTPStatus
from structure.forms import *
from datetime import date

from structure.models import Position, Employee


class UserLoginViewTest(SimpleTestCase):
    """Тест представления главной страницы"""

    def setUp(self):
        self.url = reverse('structure:login')
        self.response = self.client.get(self.url)

    def test_view_form(self):
        # Тест на соответствие формы экземпляру UserLoginForm и наличие csrf токена
        form = self.response.context_data.get('form')
        self.assertIsInstance(form, UserLoginForm)
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_view_content_test(self):
        # Тест на содержимое страницы
        self.assertEqual(self.response.status_code, HTTPStatus.OK)
        self.assertEqual(self.response.context_data['title'], 'Авторизация')
        self.assertTemplateUsed(self.response, 'structure/login.html')


class StructureCompanyTemplateViewTest(TestCase):
    """Тест представления страницы структуры компании"""

    def setUp(self):
        self.user = User.objects.create(username='test_user', password='12345')
        self.url = reverse('structure:structure_company')

    def test_view_content(self):
        # Тест на содержимое страницы
        self.client.force_login(self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Структура компании')
        self.assertTemplateUsed(response, 'structure/structure_company.html')

    def test_view_content_for_user_without_permission(self):
        # Тест на содержимое страницы для пользователя без разрешения на изменение данных
        self.client.force_login(self.user)
        response = self.client.get(self.url)
        self.assertIn('структура компании', response.content.decode())
        self.assertNotIn('найм и распределение сотрудников', response.content.decode())
        self.assertIn('выход', response.content.decode())
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_view_content_for_user_with_permission(self):
        # Тест на содержимое страницы для пользователя с разрешением на изменение данных
        self.user.user_permissions.add(Permission.objects.get(codename='change_employee'))
        self.user.save()
        self.client.force_login(self.user)
        response = self.client.get(self.url)
        self.assertIn('структура компании', response.content.decode())
        self.assertIn('найм и распределение сотрудников', response.content.decode())
        self.assertIn('выход', response.content.decode())
        self.assertEqual(response.status_code, HTTPStatus.OK)


class EmployeesViewTest(TestCase):
    """Тест представления отображающего список сотрудников с использованием фильтров и формы поиска"""

    fixtures = {'positions.json'}

    def setUp(self):
        self.user = User.objects.create(username='user', password='12345')
        self.url = reverse(
            'structure:department',
            kwargs={
                'position_id': 18,
                'order_by': 'salary',
                'direction': 'descend',
                }
            )

        positions = Position.objects.all()
        Employee.objects.create(
            first_name='Николай',
            last_name='Фролов',
            patronymic='Семёнович',
            position=positions[17],
            salary=63_000,
        )

    def test_view_content(self):
        # Тест на содержимое страницы
        self.client.force_login(self.user)
        response = self.client.get(self.url)
        form = response.context.get('form')
        self.assertIsInstance(form, SearchEmployeeForm)
        self.assertContains(response, 'csrfmiddlewaretoken')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context['title'], 'Список сотрудников')
        self.assertTemplateUsed(response, 'structure/department.html')

    def test_view_content_for_user_without_permission(self):
        # Тест на содержимое страницы для пользователя без разрешения на изменение данных
        self.client.force_login(self.user)
        response = self.client.get(self.url)
        self.assertIn('структура компании', response.content.decode())
        self.assertNotIn('найм и распределение сотрудников', response.content.decode())
        self.assertIn('выход', response.content.decode())
        self.assertNotIn('изменить', response.content.decode())
        self.assertNotIn('уволить', response.content.decode())
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_view_content_for_user_with_permission(self):
        # Тест на содержимое страницы для пользователя с разрешением на изменение данных
        self.user.user_permissions.add(Permission.objects.get(codename='change_employee'))
        self.user.save()
        self.client.force_login(self.user)
        response = self.client.get(self.url)
        self.assertIn('структура компании', response.content.decode())
        self.assertIn('найм и распределение сотрудников', response.content.decode())
        self.assertIn('выход', response.content.decode())
        self.assertIn('изменить', response.content.decode())
        self.assertIn('уволить', response.content.decode())
        self.assertEqual(response.status_code, HTTPStatus.OK)


class EmployeeDetailTest(TestCase):
    """Тест функции для возврата исходных данных, при отмене изменений данных сотрудника"""

    fixtures = {'positions.json'}

    def setUp(self):
        self.user = User.objects.create(email='test_user', password='12345')
        self.url = reverse('structure:employee_detail', kwargs={'pk': 1, 'num': 1})
        positions = Position.objects.all()
        Employee.objects.create(
            first_name='Николай',
            last_name='Фролов',
            patronymic='Семёнович',
            position=positions[17],
            salary=63_000,
        )

    def test_function(self):
        # Тест на содержимое возвращаемых данных
        self.client.force_login(self.user)
        response = self.client.get(self.url)
        self.assertIn('Николай', response.content.decode())
        self.assertIn('Фролов', response.content.decode())
        self.assertIn('Семёнович', response.content.decode())
        self.assertIn('Производственный цех 1', response.content.decode())
        self.assertIn('63000', response.content.decode())


class UpdateEmployeeDetails(TestCase):
    """Тест функции изменения данных сотрудника"""

    fixtures = {'positions.json'}

    def setUp(self):
        self.user = User.objects.create(email='test_user', password='12345')
        self.user.user_permissions.add(Permission.objects.get(codename='change_employee'))
        self.user.save()
        self.client.force_login(self.user)
        self.positions = Position.objects.all()
        Employee.objects.create(
            first_name='Николай',
            last_name='Фролов',
            patronymic='Семёнович',
            position=self.positions[17],
            salary=63_000,
        )

    def test_get_function_request(self):
        response = self.client.get(reverse('structure:update_employee_detail', kwargs={'pk': 1, 'num': 1}))
        self.assertIn('Николай', response.content.decode())
        self.assertIn('Фролов', response.content.decode())
        self.assertIn('Семёнович', response.content.decode())
        self.assertIn('Производственный цех 1', response.content.decode())
        self.assertIn('63000', response.content.decode())

    def test_post_function_request(self):
        employee_before_update = Employee.objects.filter(pk=1).first()
        self.client.post(
            reverse('structure:update_employee_detail', kwargs={'pk': 1, 'num': 1}),
            data={
                'first_name': 'Николай',
                'last_name': 'Фролов',
                'patronymic': 'Семёнович',
                'position': 1,
                'employment_date': date.today(),
                'salary': 100_000,
                }
        )

        employee_after_update = Employee.objects.filter(pk=1).first()
        self.assertEqual(employee_before_update.first_name, employee_after_update.first_name)
        self.assertEqual(employee_before_update.last_name, employee_after_update.last_name)
        self.assertEqual(employee_before_update.patronymic, employee_after_update.patronymic)
        self.assertEqual(employee_before_update.employment_date, employee_after_update.employment_date)
        self.assertEqual(employee_before_update.position, self.positions[17])
        self.assertEqual(employee_after_update.position, self.positions[0])
        self.assertEqual(employee_before_update.salary, 63_000)
        self.assertEqual(employee_after_update.salary, 100_000)
