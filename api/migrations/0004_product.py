# Generated by Django 3.2.12 on 2023-07-29 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_categories_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('discription', models.TextField()),
                ('categories', models.ManyToManyField(to='api.Categories')),
            ],
        ),
    ]