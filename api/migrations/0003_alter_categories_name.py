# Generated by Django 3.2.12 on 2023-07-29 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_categories_categore'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
