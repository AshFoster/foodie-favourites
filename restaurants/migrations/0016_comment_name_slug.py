# Generated by Django 3.2 on 2022-02-22 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0015_alter_restaurant_author_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='name_slug',
            field=models.SlugField(max_length=100, null=True),
        ),
    ]
