# Generated by Django 3.2 on 2022-01-16 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0003_auto_20220116_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dishes', to='restaurants.restaurant'),
        ),
    ]
