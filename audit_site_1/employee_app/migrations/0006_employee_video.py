# Generated by Django 4.0.1 on 2022-01-27 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_app', '0005_employee_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='video',
            field=models.FileField(default=True, upload_to='audit_site_1/media/video/employee_video/%Y/%m/%d/'),
        ),
    ]
