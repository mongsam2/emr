# Generated by Django 4.2.5 on 2023-12-16 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0027_ankle2_part_elbow2_part_knee2_part_wrist2_part'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exerciselist',
            name='date',
            field=models.DateField(),
        ),
    ]
