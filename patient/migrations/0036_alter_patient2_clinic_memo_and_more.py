# Generated by Django 4.2.5 on 2023-12-17 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0035_delete_customuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient2',
            name='clinic_memo',
            field=models.TextField(blank=True, default='물리치료 메모', null=True),
        ),
        migrations.AlterField(
            model_name='patient2',
            name='exercise_memo',
            field=models.TextField(blank=True, default='운동처방 메모', null=True),
        ),
        migrations.AlterField(
            model_name='patient2',
            name='memo',
            field=models.TextField(blank=True, default='메모', null=True),
        ),
        migrations.AlterField(
            model_name='patient2',
            name='rom_memo',
            field=models.TextField(blank=True, default='가동범위 검사 메모', null=True),
        ),
    ]