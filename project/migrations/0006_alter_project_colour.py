# Generated by Django 5.0.1 on 2024-01-21 14:52

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_alter_project_colour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='colour',
            field=colorfield.fields.ColorField(default='#1e1e1e', image_field=None, max_length=25, samples=None),
        ),
    ]
