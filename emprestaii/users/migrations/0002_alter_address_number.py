# Generated by Django 5.1.7 on 2025-03-18 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='number',
            field=models.IntegerField(),
        ),
    ]
