# Generated by Django 4.0.5 on 2022-10-09 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='classroom',
            name='description',
            field=models.CharField(default='', max_length=255),
        ),
    ]