# Generated by Django 2.2.16 on 2020-10-27 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='goods',
            old_name='click_name',
            new_name='click_num',
        ),
    ]
