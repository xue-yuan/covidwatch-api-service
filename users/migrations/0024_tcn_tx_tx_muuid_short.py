# Generated by Django 3.0.8 on 2020-07-20 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0023_auto_20200720_1946'),
    ]

    operations = [
        migrations.AddField(
            model_name='tcn_tx',
            name='tx_muuid_short',
            field=models.CharField(max_length=100, null=True),
        ),
    ]