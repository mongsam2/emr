# Generated by Django 4.2.5 on 2023-12-04 03:12

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0022_ankle_elbow_knee_shoulderhip_wrist_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShoulderHip2',
            fields=[
                ('code', models.CharField(default=uuid.uuid4, max_length=36, primary_key=True, serialize=False)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('flexion_L', models.IntegerField()),
                ('flexion_R', models.IntegerField()),
                ('extension_L', models.IntegerField()),
                ('extension_R', models.IntegerField()),
                ('lateral_rotation_L', models.IntegerField()),
                ('lateral_rotation_R', models.IntegerField()),
                ('medial_rotation_L', models.IntegerField()),
                ('medial_rotation_R', models.IntegerField()),
                ('abduction_L', models.IntegerField()),
                ('abduction_R', models.IntegerField()),
                ('adduction_L', models.IntegerField()),
                ('adduction_R', models.IntegerField()),
                ('part', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.part')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patient2')),
            ],
        ),
        migrations.DeleteModel(
            name='ShoulderHip',
        ),
    ]
