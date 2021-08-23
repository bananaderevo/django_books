# Generated by Django 3.2.6 on 2021-08-23 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Book',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(max_length=100)),
                ('books', models.TextField()),
            ],
            options={
                'verbose_name': 'Orders',
                'ordering': ['id'],
            },
        ),
    ]