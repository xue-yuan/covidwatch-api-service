# Generated by Django 3.0.8 on 2020-07-20 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_auto_20200719_1408'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttackLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log', models.TextField(null=True)),
            ],
        ),
    ]
