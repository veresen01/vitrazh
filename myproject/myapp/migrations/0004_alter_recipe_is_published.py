# Generated by Django 5.0.1 on 2024-02-06 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_recipe_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='is_published',
            field=models.BooleanField(choices=[(0, 'Черновик'), (1, 'Опубликовано')], default=0),
        ),
    ]