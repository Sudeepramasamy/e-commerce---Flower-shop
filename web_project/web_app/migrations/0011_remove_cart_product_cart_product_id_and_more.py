# Generated by Django 5.0.3 on 2024-05-21 06:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('web_app', '0010_alter_cart_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='product',
        ),
        migrations.AddField(
            model_name='cart',
            name='product_id',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='cart',
            name='product_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
    ]
