# Generated by Django 4.2.5 on 2023-12-17 07:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0034_customuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
