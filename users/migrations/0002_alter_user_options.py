# Generated by Django 4.1.5 on 2023-01-10 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={
                "ordering": ["username"],
                "verbose_name": "Пользователь",
                "verbose_name_plural": "Пользователи",
            },
        ),
    ]
