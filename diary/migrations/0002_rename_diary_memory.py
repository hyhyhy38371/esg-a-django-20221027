# Generated by Django 4.1.2 on 2022-10-27 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("diary", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="diary",
            new_name="Memory",
        ),
    ]