# Generated by Django 4.2.1 on 2023-05-17 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('favourites', '0005_alter_info_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='id',
            field=models.UUIDField(default='db26c0cfa3c74c1a811df2ad2d085117', editable=False, primary_key=True, serialize=False),
        ),
    ]
