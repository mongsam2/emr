# Generated by Django 4.2.5 on 2023-11-25 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0007_exercise_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exerciselist',
            name='count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='exerciselist',
            name='set',
            field=models.IntegerField(default=1),
        ),
    ]