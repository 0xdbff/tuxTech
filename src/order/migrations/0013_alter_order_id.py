# Generated by Django 4.2.1 on 2023-05-25 22:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("order", "0012_alter_order_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="id",
            field=models.UUIDField(
                default="3eb6092112bf47608eed43ebf33e8014",
                editable=False,
                primary_key=True,
                serialize=False,
            ),
        ),
    ]