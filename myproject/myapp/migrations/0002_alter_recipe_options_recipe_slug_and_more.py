# Generated by Django 5.0.1 on 2024-02-05 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipe',
            options={'ordering': ['-time_create']},
        ),
        migrations.AddField(
            model_name='recipe',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=255),
        ),
        migrations.AddIndex(
            model_name='recipe',
            index=models.Index(fields=['-time_create'], name='myapp_recip_time_cr_6ced72_idx'),
        ),
    ]
