# Generated by Django 3.2.6 on 2021-08-02 18:50

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('products', '0003_auto_20210802_1147'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='is_edited',
            new_name='modified',
        ),
    ]