# Generated by Django 4.0.4 on 2022-04-27 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sale_management', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='quantity',
            new_name='stock',
        ),
    ]