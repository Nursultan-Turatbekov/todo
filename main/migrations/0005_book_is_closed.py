# Generated by Django 3.1.3 on 2021-01-22 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210122_1558'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='is_closed',
            field=models.BooleanField(default=False),
        ),
    ]
