# Generated by Django 5.0.1 on 2024-02-13 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0009_board_colour_board_text_colour_boardgroup_colour_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='stage',
            name='order',
            field=models.IntegerField(default=0),
        ),
    ]
