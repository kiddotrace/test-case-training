# Generated by Django 3.2.6 on 2021-08-02 18:05

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='LOGO',
            field=models.ImageField(blank=True, upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='product',
            name='UPDATED',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='product',
            name='CREATED',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='product',
            name='ROTATE_DURATION',
            field=models.CharField(max_length=50, null=True),
        ),
    ]