# Generated by Django 3.2.7 on 2021-09-16 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20210916_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='title',
            field=models.TextField(blank=True),
        ),
    ]
