# Generated by Django 3.1.7 on 2021-05-19 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_production'),
    ]

    operations = [
        migrations.AlterField(
            model_name='production',
            name='created',
            field=models.DateTimeField(verbose_name='作成日時'),
        ),
    ]
