# Generated by Django 3.0.8 on 2020-07-20 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0022_auto_20200720_1724'),
    ]

    operations = [
        migrations.AddField(
            model_name='tcn_rx',
            name='rx_muuid_short',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tcn_rx',
            name='tx_muuid_short',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='tcn_rx',
            name='rx_muuid',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
