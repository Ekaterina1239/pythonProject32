# Generated by Django 4.2.8 on 2023-12-15 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('age', models.PositiveIntegerField()),
                ('experience_year', models.PositiveIntegerField()),
                ('vacancy', models.CharField(max_length=250)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
    ]