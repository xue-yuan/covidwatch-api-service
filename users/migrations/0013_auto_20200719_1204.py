# Generated by Django 3.0.8 on 2020-07-19 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20200719_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='expire_time',
            field=models.DateTimeField(null=True),
        ),
    ]