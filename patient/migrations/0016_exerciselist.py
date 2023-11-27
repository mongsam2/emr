# Generated by Django 4.2.5 on 2023-11-26 14:13

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0015_exercise_exercisetype_motion_part_rom_delete_ankle_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExerciseList',
            fields=[
                ('code', models.CharField(default=uuid.uuid4, max_length=36, primary_key=True, serialize=False)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('count', models.IntegerField(default=0)),
                ('set', models.IntegerField(default=1)),
                ('time', models.IntegerField(default=0)),
                ('weight', models.IntegerField(default=0)),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.exercise')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patient2')),
            ],
        ),
    ]
