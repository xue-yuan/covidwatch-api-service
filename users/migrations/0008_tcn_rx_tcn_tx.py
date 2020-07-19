# Generated by Django 3.0.8 on 2020-07-18 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20200717_2347'),
    ]

    operations = [
        migrations.CreateModel(
            name='TCN_RX',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rx_muuid', models.CharField(max_length=50)),
                ('tx_muuid', models.CharField(max_length=50)),
                ('rx_tcn', models.CharField(max_length=50)),
                ('tcn', models.CharField(max_length=50)),
                ('rssi', models.FloatField()),
                ('distance', models.FloatField()),
                ('uxix_timestamp', models.DateTimeField()),
                ('upload_timestamp', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='TCN_TX',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tx_muuid', models.CharField(max_length=50)),
                ('tx_tcn', models.CharField(max_length=50)),
                ('own_tch', models.CharField(max_length=50)),
                ('battery_level', models.IntegerField()),
                ('motion_status', models.BooleanField()),
                ('gps_status', models.BooleanField()),
                ('uxix_timestamp', models.DateTimeField()),
                ('upload_timestamp', models.DateTimeField()),
            ],
        ),
    ]
