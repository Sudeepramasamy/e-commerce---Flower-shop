# Generated by Django 5.0.3 on 2024-04-12 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='signin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='', max_length=20)),
                ('PhoneNumber', models.IntegerField(default='')),
                ('Gmail', models.CharField(default='', max_length=20)),
                ('Password', models.CharField(default='', max_length=20)),
            ],
        ),
    ]
