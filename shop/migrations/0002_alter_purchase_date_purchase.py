# Generated by Django 4.2.7 on 2023-11-19 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='date_purchase',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
