from django.db import models


class Position(models.Model):
    """Модель Должность"""
    boss = models.ForeignKey(
        'self', on_delete=models.DO_NOTHING, default=1, verbose_name='непосредственный начальник',
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
    first_name = models.CharField(max_length=50, verbose_name='имя')
    last_name = models.CharField(max_length=50, verbose_name='фамилия')
    patronymic = models.CharField(max_length=50, verbose_name='отчество')
    position = models.ForeignKey(Position, on_delete=models.SET_DEFAULT,
                                 default=1, blank=False, null=False, verbose_name='должность')
    employment_date = models.DateField(null=True, blank=True, verbose_name='дата приёма на работу')
    salary = models.IntegerField(default=0, verbose_name='зарплата')

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


# python manage shell_plus --print-sql
