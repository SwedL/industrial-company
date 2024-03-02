from django.test import TestCase

from datetime import date

from structure.models import Employee, Position


class PositionModelTest(TestCase):
    """Тест модели Position"""

    def setUp(self):
        self.position = Position(
            name='Руководитель',
            is_manager=True,
            vacancies=1,
            base_salary=100_000,
        )

    def test_create_position(self):
        self.assertIsInstance(self.position, Position)

    def test_str_representation(self):
        self.assertEqual(str(self.position), 'Руководитель')

    def test_saving_and_retrieving_position(self):
        first_position = Position()
        first_position.name = 'Руководитель'
        first_position.is_manager = True
        first_position.vacancies = 1
        first_position.base_salary = 100_000
        first_position.save()

        second_position = Position()
        second_position.name = 'Производственный цех 1'
        second_position.is_manager = True
        second_position.vacancies = 800
        second_position.base_salary = 60_000
        second_position.save()

        third_position = Position()
        third_position.name = 'Производственный цех 2'
        third_position.is_manager = False
        third_position.vacancies = 1000
        third_position.base_salary = 50_000
        third_position.save()

        saved_positions = Position.objects.all()
        self.assertEqual(saved_positions.count(), 3)

        first_saved_position = saved_positions[0]
        second_saved_position = saved_positions[1]
        self.assertEqual(first_saved_position.name, 'Руководитель')
        self.assertEqual(second_saved_position.base_salary, 60_000)
        self.assertEqual(second_saved_position.boss, first_position)


class EmployeeModelTest(TestCase):
    """Тест модели Employee"""

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
