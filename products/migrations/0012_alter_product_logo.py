# Generated by Django 3.2.6 on 2021-08-02 20:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('products', '0011_alter_product_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
