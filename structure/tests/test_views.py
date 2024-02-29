from django.test import TestCase

from datetime import date

from structure.models import Position, Employee


class IndexListViewTestCase(TestCase):
    """Тест представления главной страницы"""

    fixtures = {'services.json'}

    def setUp(self):
        self.services = CarWashService.objects.all()
        self.user = User.objects.create(email='test@mail.ru', password='test')
        self.permission = Permission.objects.get(codename='view_carwashworkday')
        self.path = reverse('carwash:home')

    def test_view_for_not_logged_user(self):
        # Проверка меню для неавторизованого пользователя
        response = self.client.get(self.path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Aquamarine')
        self.assertTemplateUsed(response, 'carwash/index.html')
        self.assertEqual(list(response.context_data['object_list']), list(self.services))
        self.assertEqual(self._common_tests(), [])

    def test_if_logged_but_cannot_permission(self):
        # Проверка отображения меню для авторизованного пользователя, без permission
        self.client.force_login(self.user)

        self.assertEqual(self._common_tests(), ['Профиль', 'Мои записи', 'Выйти'])

    def test_if_logged_and_can_permission(self):
        # Проверка отображения меню для авторизованного пользователя с permission
        self.user.user_permissions.add(self.permission)
        self.client.force_login(self.user)

        self.assertEqual(self._common_tests(), ['Профиль', 'Мои записи', 'Менеджер', 'Выйти'])

    def test_if_logged_and_can_permission_and_is_admin(self):
        # Проверка отображения меню для авторизованного пользователя, с правами admin
        self.user.user_permissions.add(self.permission)
        self.user.is_admin = True
        self.user.save()
        self.client.force_login(self.user)

        self.assertEqual(self._common_tests(), ['Профиль', 'Мои записи', 'Менеджер', 'Админ-панель', 'Выйти'])

    def _common_tests(self):
        response = self.client.get(self.path)

        soup = BeautifulSoup(response.content, 'html.parser')
        result = [r.text for r in soup.find_all('a', class_='dropdown-item')]
        return result