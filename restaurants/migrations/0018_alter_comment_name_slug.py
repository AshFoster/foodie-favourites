# Generated by Django 3.2 on 2022-02-22 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0017_remove_comment_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='name_slug',
            field=models.SlugField(max_length=100),
        ),
    ]
