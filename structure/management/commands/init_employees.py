from random import choice, uniform

from structure.models import Employee, Position
from tqdm import tqdm    # для красивой визуализации обработки данных
import time
from datetime import date, timedelta
from django.core.management.base import BaseCommand

from mimesis import Person
from mimesis.enums import Gender
from mimesis.locales import Locale
from mimesis.providers import BaseDataProvider
from mimesis.types import MissingSeed, Seed


__all__ = ["RussiaSpecProvider"]


class RussiaSpecProvider(BaseDataProvider):
    """Class that provides special data for Russia (ru)."""

    def __init__(self, seed: Seed = MissingSeed) -> None:
        """Initialize attributes."""
        super().__init__(locale=Locale.RU, seed=seed)

    class Meta:
        """The name of the provider."""

        name = "russia_provider"
        datafile = "builtin.json"

    def patronymic(self, gender: Gender | None = None) -> str:
        """Generate random patronymic name.

        :param gender: Gender of person.
        :return: Patronymic name.

        :Example:
            Алексеевна.
        """
        gender = self.validate_enum(gender, Gender)
        patronymics: list[str] = self._extract(["patronymic", str(gender)])
        return self.random.choice(patronymics)


class Command(BaseCommand):
    def handle(self, *args, **options):
        start_time = time.time()
        self.stdout.write("Наполнения базы данных сотрудниками (Employee)")

        person = Person('ru')
        patron = RussiaSpecProvider()

        # создание словаря, где key - id, value - количество доступных вакансий на должность
        vacancies_for_positions = {i.id: i.vacancies for i in Position.objects.all()}

        # список зарплат сотрудников относительно id должности ([0, 500000, ...])
        salary_list = [0] + [i.base_salary for i in Position.objects.all()]

        # 50100 количество человек желающих получить работу
        for _ in tqdm(range(50000), ncols=100, desc='Processing'):
            gender = choice([Gender.MALE, Gender.FEMALE, Gender.MALE])    # выбор пола создаваемого сотрудника
            first_name = person.first_name(gender=gender)
            last_name = person.last_name(gender=gender)
            patronymic = patron.patronymic(gender=gender)
            td = choice(range(0, 3650))    # рандомное кол-во дней назад устроился сотрудник от текущего дня
            employment_date = date.today() - timedelta(days=td)

            # выбираем должности, у которых имеются вакансии
            choice_id_position = choice(list(filter(lambda x: vacancies_for_positions[x] > 0, vacancies_for_positions)))
            choice_position = Position.objects.get(id=choice_id_position)    # выбор случайной должности
            # уменьшаем количество необходимых сотрудников, выбранной должности, на 1
            vacancies_for_positions[choice_id_position] = vacancies_for_positions.get(choice_id_position) - 1
            salary = salary_list[choice_id_position] * uniform(0.9, 1.1)    # изменение з/п на 10%
            Employee.objects.create(
                first_name=first_name,
                last_name=last_name,
                patronymic=patronymic,
                position=choice_position,
                employment_date=employment_date,
                salary=salary
            )

        for p in Position.objects.all():
            p.vacancies=vacancies_for_positions[p.id]
            p.save()

        self.stdout.write(f"Наполнение базы данных завершено за время: {str((time.time() - start_time) / 60 )} минут")


# запуск наполнения базы данных сотрудниками
# python manage.py init_employees

# удаление всех объектов Employee
# python manage.py shell_plus --print-sql
# e = Employee.objects.all()
# e.delete()

# загрузка всех объектов Position
# python manage.py loaddata company\fixtures\position.json
