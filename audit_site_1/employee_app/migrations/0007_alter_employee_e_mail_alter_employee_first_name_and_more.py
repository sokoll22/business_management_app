# Generated by Django 4.0.1 on 2022-02-01 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_app', '0006_employee_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='e_mail',
            field=models.EmailField(max_length=128),
        ),
        migrations.AlterField(
            model_name='employee',
            name='first_name',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='employee',
            name='last_name',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='employee',
            name='photo',
            field=models.ImageField(upload_to='media/image/employee_photo/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='position',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='employee',
            name='url',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='employee',
            name='video',
            field=models.FileField(default=True, upload_to='media/video/employee_video/%Y/%m/%d/'),
        ),
    ]
