# Generated by Django 3.2.12 on 2023-07-29 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categories',
            old_name='name',
            new_name='new_catagory',
        ),
    ]
