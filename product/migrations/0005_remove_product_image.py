# Generated by Django 3.2.4 on 2021-06-17 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_rename_post_productimage_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
    ]