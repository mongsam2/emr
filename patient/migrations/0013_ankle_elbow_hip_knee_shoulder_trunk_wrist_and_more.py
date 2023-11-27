# Generated by Django 4.2.5 on 2023-11-26 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0012_remove_exercise_type_delete_exercisetype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ankle',
            fields=[
                ('motion', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('arom', models.IntegerField()),
                ('prom', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Elbow',
            fields=[
                ('motion', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('arom', models.IntegerField()),
                ('prom', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Hip',
            fields=[
                ('motion', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('arom', models.IntegerField()),
                ('prom', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Knee',
            fields=[
                ('motion', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('arom', models.IntegerField()),
                ('prom', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Shoulder',
            fields=[
                ('motion', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('arom', models.IntegerField()),
                ('prom', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Trunk',
            fields=[
                ('motion', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('arom', models.IntegerField()),
                ('prom', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Wrist',
            fields=[
                ('motion', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('arom', models.IntegerField()),
                ('prom', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='exerciselist',
            name='exercise',
        ),
        migrations.RemoveField(
            model_name='exerciselist',
            name='patient',
        ),
        migrations.DeleteModel(
            name='Exercise',
        ),
        migrations.DeleteModel(
            name='ExerciseList',
        ),
    ]
