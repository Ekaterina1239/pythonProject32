# Generated by Django 4.2.8 on 2023-12-15 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]