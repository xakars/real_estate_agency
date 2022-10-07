# Generated by Django 2.2.24 on 2022-10-07 11:01

from django.db import migrations
from phonenumber_field.phonenumber import PhoneNumber
import phonenumbers


def format_phone_number(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        phone_number = phonenumbers.parse(flat.owners_phonenumber, "RU")
        if phonenumbers.is_valid_number(phone_number):
            flat.owner_pure_phone = PhoneNumber.from_string(
                phone_number=flat.owners_phonenumber,
                region='RU').as_e164
        else:
            pass
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_auto_20221007_1314'),
    ]

    operations = [
        migrations.RunPython(format_phone_number)
    ]
