# Generated by Django 4.2.1 on 2023-05-15 10:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("product", "0002_initial"),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="client",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments",
                to="users.client",
            ),
        ),
        migrations.AddField(
            model_name="comment",
            name="variant",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments",
                to="product.variant",
            ),
        ),
        migrations.AddField(
            model_name="baseinfo",
            name="brand",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="product_baseInfo",
                to="product.brand",
            ),
        ),
        migrations.AddField(
            model_name="baseinfo",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="base_info",
                to="product.category",
            ),
        ),
        migrations.AddField(
            model_name="baseinfo",
            name="ptype",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="base_info",
                to="product.type",
            ),
        ),
        migrations.AddField(
            model_name="baseinfo",
            name="subCategory",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="base_info",
                to="product.subcategory",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="variantmedia",
            unique_together={("variant", "media")},
        ),
    ]