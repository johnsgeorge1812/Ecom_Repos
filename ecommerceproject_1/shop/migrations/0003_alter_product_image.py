# Generated by Django 4.1 on 2024-02-27 13:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0002_alter_product_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="Image",
            field=models.ImageField(blank=True, default="", upload_to="product"),
        ),
    ]
