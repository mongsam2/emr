# Generated by Django 4.2.5 on 2023-11-26 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0009_exercisepart_type_alter_exercise_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Neck',
            fields=[
                ('motion', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('arom', models.IntegerField()),
                ('prom', models.IntegerField()),
            ],
        ),
    ]
