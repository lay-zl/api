# Generated by Django 3.2.12 on 2023-07-30 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_product_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='categore',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='api.categories'),
        ),
    ]
