# Generated by Django 4.1.7 on 2023-11-27 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_rename_tasarimlarim_design'),
    ]

    operations = [
        migrations.AlterField(
            model_name='design',
            name='img',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='kartlar',
            name='img',
            field=models.ImageField(upload_to='images/'),
        ),
    ]