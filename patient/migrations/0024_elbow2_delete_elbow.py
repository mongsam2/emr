# Generated by Django 4.2.5 on 2023-12-04 03:29

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0023_shoulderhip2_delete_shoulderhip'),
    ]

    operations = [
        migrations.CreateModel(
            name='Elbow2',
            fields=[
                ('code', models.CharField(default=uuid.uuid4, max_length=36, primary_key=True, serialize=False)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('flexion_L', models.IntegerField()),
                ('flexion_R', models.IntegerField()),
                ('extension_L', models.IntegerField()),
                ('extension_R', models.IntegerField()),
                ('pronation_L', models.IntegerField()),
                ('pronation_R', models.IntegerField()),
                ('supination_L', models.IntegerField()),
                ('supination_R', models.IntegerField()),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patient2')),
            ],
        ),
        migrations.DeleteModel(
            name='Elbow',
        ),
    ]
