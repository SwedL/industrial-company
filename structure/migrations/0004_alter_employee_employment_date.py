# Generated by Django 5.0.1 on 2024-03-04 07:55

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0003_employee_hr_employee_salary_ix'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='employment_date',
            field=models.DateField(db_index=True, default=django.utils.timezone.now, verbose_name='дата приёма на работу'),
        ),
    ]