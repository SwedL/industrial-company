from datetime import date

from django.test import TestCase

from structure.models import Employee, Position


class PositionModelTest(TestCase):
    """ Тест модели Position """

    fixtures = {'positions.json'}

    def setUp(self):
        main_position = Position.objects.first()
        self.new_position = Position.objects.create(
            boss=main_position,
            name='Начальник ВОХР',
            is_manager=True,
            vacancies=1,
            base_salary=100_000,
        )

    def test_create_position(self):
        self.assertIsInstance(self.new_position, Position)
        self.assertEqual(str(self.new_position.boss), 'Руководитель')
        self.assertEqual(self.new_position.name, 'Начальник ВОХР')
        self.assertTrue(self.new_position.is_manager)
        self.assertEqual(self.new_position.vacancies, 1)
        self.assertEqual(self.new_position.base_salary, 100_000)

    def test_str_representation(self):
        self.assertEqual(str(self.new_position), 'Начальник ВОХР')


class EmployeeModelTest(TestCase):
    """ Тест модели Employee """

    fixtures = {'positions.json'}

    def setUp(self):
        self.positions = Position.objects.all()
        self.employee = Employee()
        self.employee.first_name = 'Николай'
        self.employee.last_name = 'Фролов'
        self.employee.patronymic = 'Семёнович'
        self.employee.position = self.positions[17]
        self.employee.salary = 63_000

    def test_create_employee(self):
        self.assertIsInstance(self.employee, Employee)

    def test_str_representation(self):
        self.assertEqual(str(self.employee), 'Фролов')

    def test_count_position(self):
        self.assertEqual(self.positions.count(), 47)

    def test_saving_and_retrieving_employee(self):
        Employee.objects.create(
            first_name='Николай',
            last_name='Фролов',
            patronymic='Семёнович',
            position=self.positions[17],
            salary=63_000,
        )

        Employee.objects.create(
            first_name='Михаил',
            last_name='Гурьев',
            patronymic='Васильевич',
            position=self.positions[19],
            salary=53_000,
        )

        employees = Employee.objects.all()
        self.assertEqual(employees.count(), 2)

        first_employee = employees[0]
        second_employee = employees[1]
        self.assertEqual(first_employee.first_name, 'Николай')
        self.assertEqual(first_employee.salary, 63_000)
        self.assertEqual(first_employee.employment_date, date.today())
        self.assertEqual(second_employee.last_name, 'Гурьев')
        self.assertEqual(second_employee.salary, 53_000)
        self.assertEqual(second_employee.employment_date, date.today())
