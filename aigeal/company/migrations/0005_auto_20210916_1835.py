# Generated by Django 3.2.7 on 2021-09-16 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_auto_20210916_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offering',
            name='image',
            field=models.FileField(upload_to='media'),
        ),
        migrations.AlterField(
            model_name='offering',
            name='image_light',
            field=models.FileField(null=True, upload_to='media'),
        ),
    ]
