# Generated by Django 4.0.1 on 2022-02-01 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_app', '0007_alter_employee_e_mail_alter_employee_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='photo',
            field=models.ImageField(default=True, upload_to='media/image/employee_photo/%Y/%m/%d/'),
        ),
    ]
