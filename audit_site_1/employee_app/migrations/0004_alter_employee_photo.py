# Generated by Django 4.0.1 on 2022-01-24 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_app', '0003_delete_cocktail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='photo',
            field=models.ImageField(upload_to='audit_site_1/media/image/employee_photo/%Y/%m/%d/'),
        ),
    ]
