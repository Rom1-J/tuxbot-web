# Generated by Django 3.0.11 on 2021-02-08 22:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0003_auto_20210208_2300"),
    ]

    operations = [
        migrations.RenameField(
            model_name="contact",
            old_name="replied",
            new_name="answered",
        ),
    ]