# Generated by Django 4.1.4 on 2024-02-05 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='category',
            field=models.CharField(max_length=40, unique=True),
        ),
    ]
