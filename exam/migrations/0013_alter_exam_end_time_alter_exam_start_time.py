# Generated by Django 4.0.5 on 2022-11-22 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0012_alter_exam_end_time_alter_exam_start_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='end_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='exam',
            name='start_time',
            field=models.DateTimeField(),
        ),
    ]