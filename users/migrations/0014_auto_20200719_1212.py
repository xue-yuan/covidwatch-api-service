# Generated by Django 3.0.8 on 2020-07-19 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20200719_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='exp_id',
            field=models.CharField(max_length=2, null=True),
        ),
    ]
