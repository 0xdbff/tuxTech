# Generated by Django 4.2.1 on 2023-05-31 20:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("favourites", "0016_alter_info_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="info",
            name="id",
            field=models.UUIDField(
                default="fe84760c3b6c492e9165d21d5aa96dab",
                editable=False,
                primary_key=True,
                serialize=False,
            ),
        ),
    ]