# Generated by Django 5.0.3 on 2024-04-01 17:55

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0002_rename_mame_product_name_alter_product_price"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product",
            old_name="Name",
            new_name="name",
        ),
    ]