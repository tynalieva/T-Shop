# Generated by Django 3.2.4 on 2021-06-17 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productimage',
            old_name='post',
            new_name='product',
        ),
    ]