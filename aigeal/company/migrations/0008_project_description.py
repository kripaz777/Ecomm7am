# Generated by Django 3.2.7 on 2021-09-16 14:33

from django.db import migrations
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0007_solution'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='description',
            field=djrichtextfield.models.RichTextField(blank=True),
        ),
    ]