# Generated by Django 4.0.5 on 2022-10-11 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0004_classroom_code_classroom_course_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='code',
            field=models.CharField(editable=False, max_length=255),
        ),
    ]
