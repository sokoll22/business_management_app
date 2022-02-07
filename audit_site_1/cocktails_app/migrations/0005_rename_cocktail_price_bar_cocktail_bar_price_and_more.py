# Generated by Django 4.0.1 on 2022-02-04 21:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cocktails_app', '0004_alter_cocktail_cocktail_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cocktail',
            old_name='cocktail_price_bar',
            new_name='bar_price',
        ),
        migrations.RenameField(
            model_name='cocktail',
            old_name='cocktail_price_club',
            new_name='club_price',
        ),
        migrations.RenameField(
            model_name='cocktail',
            old_name='cocktail_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='cocktail',
            old_name='cocktail_price_employee',
            new_name='employee_price',
        ),
        migrations.RenameField(
            model_name='cocktail',
            old_name='cocktail_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='cocktail',
            old_name='cocktail_photo',
            new_name='photo',
        ),
    ]
