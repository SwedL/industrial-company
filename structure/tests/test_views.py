from django.test import SimpleTestCase, TestCase
from django.contrib.auth.models import User, Permission
from django.urls import reverse

from http import HTTPStatus
from structure.forms import AddEmployeeForm, SearchEmployeeForm, UpdateEmployeeDetailForm, UserLoginForm
from datetime import date

from structure.models import Position, Employee


positions = Position.objects.all()
permission = Permission.objects.get(codename='change_employee')


def common_func():
    # Общая функция для создания тестовых сотрудников
    Employee.objects.create(
        first_name='Николай',
        last_name='Фролов',
        patronymic='Семёнович',
        position=positions[17],
        salary=63_000,
    )
    Employee.objects.create(
        first_name='Михаил',
        last_name='Гурьев',
        patronymic='Васильевич',
        position=positions[19],
        salary=53_000,
    )


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
        self.user.user_permissions.add(permission)
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
        common_func()

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
        self.user.user_permissions.add(permission)
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
    """Тест функции возврата исходных данных, при отмене изменений данных сотрудника"""

    fixtures = {'positions.json'}

    def setUp(self):
        self.user = User.objects.create(email='test_user', password='12345')
        self.url = reverse('structure:employee_detail', kwargs={'pk': 1, 'num': 1})
        common_func()

    def test_get_request_function(self):
        # Проверяем содержимое возвращаемых данных
        self.client.force_login(self.user)
        response = self.client.get(self.url)
        employee = response.context['employee']
        self.assertEqual(employee.first_name, 'Николай')
        self.assertEqual(employee.last_name, 'Фролов')
        self.assertEqual(employee.patronymic, 'Семёнович')
        self.assertEqual(employee.position, positions[17])
        self.assertEqual(employee.employment_date, date.today())
        self.assertEqual(employee.salary, 63_000)


class UpdateEmployeeDetails(TestCase):
    """Тест функции изменения данных сотрудника"""

    fixtures = {'positions.json'}

    def setUp(self):
        self.user = User.objects.create(email='test_user', password='12345')
        self.user.user_permissions.add(permission)
        self.user.save()
        self.client.force_login(self.user)
        common_func()

    def test_get_function_request(self):
        # Тест get запроса функции. Проверяем полученные данных.
        response = self.client.get(reverse('structure:update_employee_detail', kwargs={'employee_id': 1, 'employee_num': 1}))
        employee = response.context['employee']
        self.assertIsInstance(response.context['form'], UpdateEmployeeDetailForm)
        self.assertEqual(employee.first_name, 'Николай')
        self.assertEqual(employee.last_name, 'Фролов')
        self.assertEqual(employee.patronymic, 'Семёнович')
        self.assertEqual(employee.position, positions[17])
        self.assertEqual(employee.employment_date, date.today())
        self.assertEqual(employee.salary, 63_000)

    def test_post_function_request(self):
        # Тест post запроса функции. Проверяем что сотрудник сменил должность и зарплату,
        # у предыдущей должности добавилась вакансия, а у текущей должности вакансия уменьшилась
        employee_before_update = Employee.objects.filter(pk=1).first()
        number_vacancies_position_17_before_update_employee = positions[17].vacancies
        number_vacancies_position_0_before_update_employee = positions[0].vacancies

        self.client.post(
            reverse('structure:update_employee_detail', kwargs={'employee_id': 1, 'employee_num': 1}),
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
        number_vacancies_position_17_after_update_employee = positions[17].vacancies
        number_vacancies_position_0_after_update_employee = positions[0].vacancies
        self.assertEqual(employee_before_update.first_name, employee_after_update.first_name)
        self.assertEqual(employee_before_update.last_name, employee_after_update.last_name)
        self.assertEqual(employee_before_update.patronymic, employee_after_update.patronymic)
        self.assertEqual(employee_before_update.employment_date, employee_after_update.employment_date)
        self.assertEqual(employee_before_update.position, positions[17])
        self.assertEqual(employee_after_update.position, positions[0])
        self.assertEqual(employee_before_update.salary, 63_000)
        self.assertEqual(employee_after_update.salary, 100_000)
        self.assertEqual(number_vacancies_position_17_before_update_employee, 11_000)
        self.assertEqual(number_vacancies_position_0_before_update_employee, 1)
        self.assertEqual(number_vacancies_position_17_after_update_employee, 11_001)
        self.assertEqual(number_vacancies_position_0_after_update_employee, 0)


class DeleteEmployee(TestCase):
    """Тест функции удаления сотрудника из БД (увольнение)"""

    fixtures = {'positions.json'}

    def setUp(self):
        self.user = User.objects.create(email='test_user', password='12345')
        common_func()

    def test_delete_employee_function(self):
        # Проверяем что кол-во сотрудников сократилось на 1, а также добавилась вакансия его должности
        self.user.user_permissions.add(permission)
        self.user.save()
        self.client.force_login(self.user)
        number_employees_before_delete_employee = Employee.objects.all().count()
        number_vacancies_position_before_delete_employee = positions[17].vacancies
        self.client.delete(reverse('structure:delete_employee', kwargs={'pk': 1}))
        number_employees_after_delete_employee = Employee.objects.all().count()
        number_vacancies_position_after_delete_employee = positions[17].vacancies
        self.assertEqual(number_employees_before_delete_employee, 2)
        self.assertEqual(number_employees_after_delete_employee, 1)
        self.assertEqual(number_vacancies_position_before_delete_employee, 11000)
        self.assertEqual(number_vacancies_position_after_delete_employee, 11001)


class EmployeeCreateViewTest(TestCase):
    """Тест представления найма и распределения сотрудников"""

    fixtures = {'positions.json'}

    def setUp(self):
        self.user = User.objects.create(email='test_user', password='12345')
        self.user.user_permissions.add(permission)
        self.user.save()
        self.client.force_login(self.user)
        self.response = self.client.get(reverse('structure:recruit_distribution'))

    def test_view_form(self):
        # Тест на соответствие формы экземпляру AddEmployeeForm и наличие csrf токена
        form = self.response.context_data.get('form')
        self.assertContains(self.response, 'csrfmiddlewaretoken')
        self.assertIsInstance(form, AddEmployeeForm)

    def test_view_content_test(self):
        # Тест на содержимое страницы
        self.assertEqual(self.response.status_code, HTTPStatus.OK)
        self.assertEqual(self.response.context_data['title'], 'Найм и распределение')
        self.assertTemplateUsed(self.response, 'structure/recruit_distribution.html')



