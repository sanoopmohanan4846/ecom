# Generated by Django 5.1.4 on 2024-12-09 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0004_profile_old_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='rate',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7),
        ),
    ]