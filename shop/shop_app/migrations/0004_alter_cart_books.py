# Generated by Django 3.2.6 on 2021-09-14 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0003_alter_cart_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='books',
            field=models.JSONField(),
        ),
    ]
