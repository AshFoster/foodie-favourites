# Generated by Django 3.2 on 2022-02-12 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_profile_favourite_cuisine'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='favourite_cuisine',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
