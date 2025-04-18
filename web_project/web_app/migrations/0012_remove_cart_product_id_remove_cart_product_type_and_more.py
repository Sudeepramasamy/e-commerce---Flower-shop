# Generated by Django 5.0.3 on 2024-05-22 08:04

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0011_remove_cart_product_cart_product_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='product_id',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='product_type',
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthday', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_app.birthday')),
                ('loversday', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_app.loversday')),
                ('mothersday', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_app.mothersday')),
                ('posy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_app.posybouquet')),
                ('waterfall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_app.waterfall')),
                ('wedding', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_app.wedding')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='web_app.products'),
            preserve_default=False,
        ),
    ]
