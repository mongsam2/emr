# Generated by Django 4.2.5 on 2023-11-26 13:43

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0014_alter_ankle_arom_alter_ankle_prom_alter_elbow_arom_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('link', models.URLField(default='https://blog.naver.com/smile86/221055278905')),
            ],
        ),
        migrations.CreateModel(
            name='ExerciseType',
            fields=[
                ('type', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Motion',
            fields=[
                ('motion', models.CharField(max_length=8, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Part',
            fields=[
                ('part', models.CharField(max_length=10, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Rom',
            fields=[
                ('code', models.CharField(default=uuid.uuid4, max_length=36, primary_key=True, serialize=False)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('arom', models.IntegerField(default=0)),
                ('other_arom', models.IntegerField(default=0)),
                ('prom', models.IntegerField(default=0)),
                ('other_prom', models.IntegerField(default=0)),
                ('motion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.motion')),
                ('part', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.part')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patient2')),
            ],
        ),
        migrations.DeleteModel(
            name='Ankle',
        ),
        migrations.DeleteModel(
            name='Elbow',
        ),
        migrations.DeleteModel(
            name='Hip',
        ),
        migrations.DeleteModel(
            name='Knee',
        ),
        migrations.DeleteModel(
            name='Neck',
        ),
        migrations.DeleteModel(
            name='Shoulder',
        ),
        migrations.DeleteModel(
            name='Trunk',
        ),
        migrations.DeleteModel(
            name='Wrist',
        ),
        migrations.AddField(
            model_name='exercise',
            name='part',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.part'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.exercisetype'),
        ),
    ]