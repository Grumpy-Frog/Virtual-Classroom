# Generated by Django 4.1.1 on 2022-11-22 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0011_alter_articlecomment_comment_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlecomment',
            name='comment_image',
            field=models.FileField(blank=True, null=True, upload_to='comment'),
        ),
    ]
