# Generated by Django 3.2.6 on 2021-08-09 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('slug', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to='media')),
                ('rank', models.IntegerField(unique=True)),
            ],
        ),
    ]
