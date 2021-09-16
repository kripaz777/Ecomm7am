# Generated by Django 3.2.7 on 2021-09-16 14:51

from django.db import migrations, models
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0008_project_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='media')),
                ('slug', models.CharField(max_length=500, unique=True)),
                ('description', djrichtextfield.models.RichTextField(blank=True)),
            ],
        ),
    ]
