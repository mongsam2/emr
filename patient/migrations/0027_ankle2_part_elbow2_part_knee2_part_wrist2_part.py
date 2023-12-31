# Generated by Django 4.2.5 on 2023-12-04 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0026_rename_necktruck_necktrunck'),
    ]

    operations = [
        migrations.AddField(
            model_name='ankle2',
            name='part',
            field=models.ForeignKey(default='발목', on_delete=django.db.models.deletion.CASCADE, to='patient.part'),
        ),
        migrations.AddField(
            model_name='elbow2',
            name='part',
            field=models.ForeignKey(default='팔꿈치', on_delete=django.db.models.deletion.CASCADE, to='patient.part'),
        ),
        migrations.AddField(
            model_name='knee2',
            name='part',
            field=models.ForeignKey(default='무릎', on_delete=django.db.models.deletion.CASCADE, to='patient.part'),
        ),
        migrations.AddField(
            model_name='wrist2',
            name='part',
            field=models.ForeignKey(default='손목', on_delete=django.db.models.deletion.CASCADE, to='patient.part'),
        ),
    ]
