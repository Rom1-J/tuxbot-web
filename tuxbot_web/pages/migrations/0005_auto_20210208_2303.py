# Generated by Django 3.0.11 on 2021-02-08 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20210208_2302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='answered',
            field=models.BooleanField(default=False, verbose_name='Answered'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='read',
            field=models.BooleanField(default=False, verbose_name='Read'),
        ),
    ]
