# Generated by Django 4.0.5 on 2022-11-19 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0003_alter_exam_name_alter_examquestion_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='examquestion',
            name='name',
        ),
        migrations.RemoveField(
            model_name='question_paper',
            name='name',
        ),
    ]
