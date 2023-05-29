# Generated by Django 4.2.1 on 2023-05-25 22:56

from django.db import migrations, models
import product.models.variant


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0003_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="variant",
            name="mediafiles_hash",
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name="variant",
            name="sku",
            field=models.CharField(
                default=product.models.variant.generate_unique_sku,
                editable=False,
                max_length=70,
                primary_key=True,
                serialize=False,
            ),
        ),
    ]