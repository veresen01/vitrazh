# Generated by Django 5.0.1 on 2024-02-06 14:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_category_recipe_cat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='cat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='myapp.category'),
        ),
    ]
