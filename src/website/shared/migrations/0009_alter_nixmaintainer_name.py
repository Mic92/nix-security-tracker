# Generated by Django 4.2.7 on 2023-12-05 04:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shared", "0008_alter_nixmaintainer_github_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="nixmaintainer",
            name="name",
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
