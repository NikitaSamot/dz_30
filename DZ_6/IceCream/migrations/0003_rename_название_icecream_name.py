# Generated by Django 4.1.5 on 2023-01-25 05:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('IceCream', '0002_rename_name_icecream_название'),
    ]

    operations = [
        migrations.RenameField(
            model_name='icecream',
            old_name='Название',
            new_name='name',
        ),
    ]
