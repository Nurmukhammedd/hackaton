# Generated by Django 3.2.7 on 2022-05-18 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20220518_1259'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='maker',
            new_name='brand',
        ),
    ]