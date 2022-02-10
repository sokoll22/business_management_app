# Generated by Django 4.0.1 on 2022-01-23 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='pnone_number',
            new_name='phone_number',
        ),
        migrations.AddField(
            model_name='employee',
            name='employee_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='cocktail',
            name='cocktail_description',
            field=models.TextField(blank=True, default=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='e_mail',
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name='employee',
            name='photo',
            field=models.ImageField(upload_to='employee_photo/%Y/%m/%d/'),
        ),
    ]
