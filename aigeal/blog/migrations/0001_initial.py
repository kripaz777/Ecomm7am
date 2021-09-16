# Generated by Django 3.2.7 on 2021-09-15 15:57

from django.db import migrations, models
import djrichtextfield.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('slug', models.TextField(unique=True)),
                ('author', models.CharField(max_length=500)),
                ('author_image', models.ImageField(upload_to='media')),
                ('description', djrichtextfield.models.RichTextField()),
                ('banner', models.ImageField(upload_to='media')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
