# Generated by Django 4.1.5 on 2023-01-13 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('changed_values_url', models.URLField(max_length=255)),
                ('uniquevalues_one_url', models.URLField(max_length=255)),
                ('uniquevalues_two_url', models.URLField(max_length=255)),
            ],
        ),
    ]