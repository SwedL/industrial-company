from django.contrib.postgres.indexes import HashIndex
from django.db import models
from django.utils import timezone


class Position(models.Model):
    """ Модель должность """

    boss = models.ForeignKey(
        'self',
        on_delete=models.DO_NOTHING,
        default=1,
        verbose_name='непосредственный начальник',
        blank=True,
    )
    name = models.CharField(max_length=150, unique=True, blank=False, verbose_name='должность')
    is_manager = models.BooleanField(default=False, verbose_name='менеджер')
    vacancies = models.PositiveSmallIntegerField(default=1, verbose_name='количество вакансий')
    base_salary = models.PositiveIntegerField(default=0, verbose_name='базовая зарплата')

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

    def __str__(self):
        return self.name


class Employee(models.Model):
    """ Модель сотрудник """

    first_name = models.CharField(max_length=50, verbose_name='имя', db_index=True)
    last_name = models.CharField(max_length=50, verbose_name='фамилия', db_index=True)
    patronymic = models.CharField(max_length=50, verbose_name='отчество', db_index=True)
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='должность')
    employment_date = models.DateField(default=timezone.now, verbose_name='дата приёма на работу', db_index=True)
    salary = models.IntegerField(default=0, verbose_name='зарплата')

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

        indexes = (
            HashIndex(
                fields=('salary',),
                name="hr_%(class)s_salary_ix",
            ),
        )

    def __str__(self):
        return self.last_name

# python manage.py shell_plus --print-sql
