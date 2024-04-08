from http import HTTPStatus

from django.contrib.auth.models import Permission, User
from django.test import TestCase
from django.urls import reverse
from django.urls.base import resolve

from structure.views import (EmployeeCreateView, EmployeesView,
                             StructureCompanyTemplateView, UserLoginView,
                             clear_search, delete_employee, employee_detail,
                             update_employee_details)


class StructureURLsTest(TestCase):
    """ Тестируем URLs """

    fixtures = {'positions.json'}

    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='12345')
        self.permission = Permission.objects.get(codename='change_employee')

    # тест url ''
    def test_root_url_resolves_to_homepage_view(self):
        found = resolve(reverse('structure:login'))
        self.assertEqual(found.func.view_class, UserLoginView)

    def test_homepage_url(self):
        response = self.client.get(reverse('structure:login'))
        self.assertEqual(response.status_code, HTTPStatus.OK)

    # тест url 'structure-company/'
    def test_root_url_resolves_to_structure_company_view(self):
        found = resolve(reverse('structure:structure_company'))
        self.assertEqual(found.func.view_class, StructureCompanyTemplateView)

    def test_structure_company_url_as_unauthorized_user(self):
        response = self.client.get(reverse('structure:structure_company'))
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def test_structure_company_url_as_an_authorized_user(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('structure:structure_company'))
        self.assertEqual(response.context_data['title'], 'Структура компании')
        self.assertTemplateUsed(response, 'structure/structure_company.html')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    # тест url 'department/<order_by>/<direction>/'
    #    и url 'department/<int:position_id>/<order_by>/<direction>/'
    def test_root_url_resolves_to_department_view_without_position_id(self):
        found = resolve(reverse('structure:department', kwargs={
            'order_by': 'salary',
            'direction': 'descend',
        }))
        self.assertEqual(found.func.view_class, EmployeesView)

    def test_root_url_resolves_to_department_view_with_position_id(self):
        found = resolve(reverse('structure:department', kwargs={
            'position_id': 18,
            'order_by': 'salary',
            'direction': 'descend',
        }))
        self.assertEqual(found.func.view_class, EmployeesView)

    def test_department_url_as_an_unauthorized_user(self):
        response = self.client.get(reverse('structure:department', kwargs={
            'position_id': 18,
            'order_by': 'salary',
            'direction': 'descend',
        }))
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def test_department_url_as_an_authorized_user(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('structure:department', kwargs={
            'position_id': 18,
            'order_by': 'salary',
            'direction': 'descend',
        }))
        self.assertEqual(response.status_code, HTTPStatus.OK)

    # тест url 'clear-search/'
    def test_root_url_resolves_to_clear_search(self):
        found = resolve(reverse('structure:clear_search'))
        self.assertEqual(found.func, clear_search)

    def test_clear_search_url_as_an_unauthorized_user(self):
        response = self.client.get(reverse('structure:clear_search'))
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def test_clear_search_url_as_an_authorized_user(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('structure:clear_search'))
        self.assertEqual(response.status_code, HTTPStatus.OK)

    # тест url 'employee-detail/<int:pk>/<int:num>/'
    def test_root_url_resolves_to_employee_detail(self):
        found = resolve(reverse('structure:employee_detail', kwargs={
            'pk': 1,
            'num': 1,
        }))
        self.assertEqual(found.func, employee_detail)

    def test_employee_detail_url_as_an_unauthorized_user(self):
        response = self.client.get(reverse('structure:employee_detail', kwargs={
            'pk': 1,
            'num': 1,
        }))
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def test_employee_detail_url_as_an_authorized_user(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('structure:employee_detail', kwargs={
            'pk': 1,
            'num': 1,
        }))
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)

    # тест url 'update_employee_detail/<int:employee_id >/<int:employee_num>'
    def test_root_url_resolves_to_update_employee_detail(self):
        found = resolve(reverse('structure:update_employee_detail', kwargs={
            'employee_id': 1,
            'employee_num': 1,
        }))
        self.assertEqual(found.func, update_employee_details)

    def test_update_employee_detail_url_as_an_unauthorized_user(self):
        response = self.client.get(reverse('structure:update_employee_detail', kwargs={
            'employee_id': 1,
            'employee_num': 1,
        }))
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def test_update_employee_detail_url_as_an_authorized_user_without_permission(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('structure:update_employee_detail', kwargs={
            'employee_id': 1,
            'employee_num': 1,
        }))
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def test_update_employee_detail_url_as_an_authorized_user_with_permission(self):
        self.user.user_permissions.add(self.permission)
        self.user.save()
        self.client.force_login(self.user)
        response = self.client.get(reverse('structure:update_employee_detail', kwargs={
            'employee_id': 1,
            'employee_num': 1,
        }))
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)

    # тест url 'delete-employee/<int:pk>/'
    def test_root_url_resolves_to_delete_employee(self):
        found = resolve(reverse('structure:delete_employee', kwargs={'pk': 1}))
        self.assertEqual(found.func, delete_employee)

    def test_delete_employee_url_as_an_unauthorized_user(self):
        response = self.client.get(reverse('structure:delete_employee', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def test_delete_employee_url_as_an_authorized_user_without_permission(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('structure:delete_employee', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def test_delete_employee_url_by_an_authorized_user_with_permission(self):
        self.user.user_permissions.add(self.permission)
        self.user.save()
        self.client.force_login(self.user)
        response = self.client.delete(reverse('structure:delete_employee', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)

    # тест url 'recruit_distribution/'
    def test_root_url_resolves_to_recruit_distribution(self):
        found = resolve(reverse('structure:recruit_distribution'))
        self.assertEqual(found.func.view_class, EmployeeCreateView)

    def test_recruit_distribution_url_as_an_unauthorized_user(self):
        response = self.client.get(reverse('structure:recruit_distribution'))
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def test_recruit_distribution_url_as_an_authorized_user_without_permission(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('structure:recruit_distribution'))
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)

    def test_recruit_distribution_url_as_an_authorized_user_with_permission(self):
        self.user.user_permissions.add(self.permission)
        self.user.save()
        self.client.force_login(self.user)
        response = self.client.get(reverse('structure:recruit_distribution'))
        self.assertEqual(response.status_code, HTTPStatus.OK)
