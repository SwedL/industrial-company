# Generated by Django 5.0.3 on 2024-04-03 11:11

import django.contrib.postgres.indexes
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='должность')),
                ('is_manager', models.BooleanField(default=False, verbose_name='менеджер')),
                ('vacancies', models.PositiveSmallIntegerField(default=1, verbose_name='количество вакансий')),
                ('base_salary', models.PositiveIntegerField(default=0, verbose_name='базовая зарплата')),
                ('boss', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='structure.position', verbose_name='непосредственный начальник')),
            ],
            options={
                'verbose_name': 'Должность',
                'verbose_name_plural': 'Должности',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(db_index=True, max_length=50, verbose_name='имя')),
                ('last_name', models.CharField(db_index=True, max_length=50, verbose_name='фамилия')),
                ('patronymic', models.CharField(db_index=True, max_length=50, verbose_name='отчество')),
                ('employment_date', models.DateField(db_index=True, default=django.utils.timezone.now, verbose_name='дата приёма на работу')),
                ('salary', models.IntegerField(default=0, verbose_name='зарплата')),
                ('position', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='structure.position', verbose_name='должность')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
                'indexes': [django.contrib.postgres.indexes.HashIndex(fields=['salary'], name='hr_employee_salary_ix')],
            },
        ),
    ]
