# Generated by Django 4.2.5 on 2023-11-25 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0006_alter_patient2_front_resident'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='link',
            field=models.URLField(default='https://www.youtube.com/watch?v=7yksitiRlfk'),
        ),
    ]
