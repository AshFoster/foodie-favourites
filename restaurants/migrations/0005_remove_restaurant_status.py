# Generated by Django 3.2 on 2022-01-17 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0004_alter_dish_restaurant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='status',
        ),
    ]
