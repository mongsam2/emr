# Generated by Django 4.2.5 on 2023-12-03 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0017_exerciselist_done'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rom',
            old_name='arom',
            new_name='other_rom',
        ),
        migrations.RenameField(
            model_name='rom',
            old_name='other_arom',
            new_name='rom',
        ),
        migrations.RemoveField(
            model_name='rom',
            name='other_prom',
        ),
        migrations.RemoveField(
            model_name='rom',
            name='prom',
        ),
    ]