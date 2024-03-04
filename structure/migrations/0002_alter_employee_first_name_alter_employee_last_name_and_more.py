# Generated by Django 5.0.1 on 2024-03-04 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='first_name',
            field=models.CharField(db_index=True, max_length=50, verbose_name='имя'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='last_name',
            field=models.CharField(db_index=True, max_length=50, verbose_name='фамилия'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='patronymic',
            field=models.CharField(db_index=True, max_length=50, verbose_name='отчество'),
        ),
    ]
