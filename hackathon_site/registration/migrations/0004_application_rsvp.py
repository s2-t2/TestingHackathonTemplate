# Generated by Django 3.1.1 on 2020-09-19 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("registration", "0003_auto_20200912_2204"),
    ]

    operations = [
        migrations.AddField(
            model_name="application", name="rsvp", field=models.BooleanField(null=True),
        ),
    ]