# Generated by Django 4.1.5 on 2023-01-13 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='changed_values_url',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='files',
            name='uniquevalues_one_url',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='files',
            name='uniquevalues_two_url',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
    ]
