# Generated by Django 4.1.7 on 2023-03-15 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_cart_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
