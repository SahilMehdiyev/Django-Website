# Generated by Django 4.1.7 on 2023-11-26 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_kartlar_tasarimlarim'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasarimlarim',
            name='url',
            field=models.TextField(max_length=100),
        ),
    ]
