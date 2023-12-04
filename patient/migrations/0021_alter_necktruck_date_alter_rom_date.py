# Generated by Django 4.2.5 on 2023-12-03 11:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0020_alter_necktruck_date_alter_rom_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='necktruck',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='rom',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
