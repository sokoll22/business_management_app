# Generated by Django 4.0.1 on 2022-02-05 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_app', '0010_alter_employee_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'ordering': ['-employee_status'], 'verbose_name': 'Сотрудник', 'verbose_name_plural': 'Список сотрудников'},
        ),
        migrations.AlterField(
            model_name='employee',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата внесения в базу'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='employee_status',
            field=models.BooleanField(default=False, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='first_name',
            field=models.CharField(max_length=64, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='interest_50',
            field=models.IntegerField(verbose_name='Чаевые 50%'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='interest_bar',
            field=models.IntegerField(verbose_name='Процент с бара'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='last_name',
            field=models.CharField(max_length=64, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='notes',
            field=models.TextField(max_length=256, verbose_name='Заметки о сотруднике'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='phone_number',
            field=models.IntegerField(verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='position',
            field=models.CharField(max_length=64, verbose_name='Должность'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='rate',
            field=models.IntegerField(verbose_name='Ставка'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='reason_of_disemployment',
            field=models.TextField(max_length=256, verbose_name='Причина увольнения'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Последнее изменение'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='url',
            field=models.CharField(max_length=256, verbose_name='Ссылка на личную страницу'),
        ),
    ]
