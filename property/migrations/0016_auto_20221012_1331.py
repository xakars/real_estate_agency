# Generated by Django 2.2.28 on 2022-10-12 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0015_auto_20221011_1505'),
    ]

    operations = [
        migrations.RenameField(
            model_name='owner',
            old_name='owner',
            new_name='name',
        ),
    ]
