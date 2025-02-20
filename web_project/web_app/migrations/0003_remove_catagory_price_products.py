# Generated by Django 5.0.3 on 2024-04-21 05:56

import django.db.models.deletion
import web_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0002_catagory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catagory',
            name='price',
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to=web_app.models.getFileName)),
                ('description', models.TextField(max_length=500)),
                ('price', models.IntegerField()),
                ('catagory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_app.catagory')),
            ],
        ),
    ]
