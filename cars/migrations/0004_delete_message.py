# Generated by Django 5.0.1 on 2024-02-10 11:45

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("cars", "0003_message"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Message",
        ),
    ]
