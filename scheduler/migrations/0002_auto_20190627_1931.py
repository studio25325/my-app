# Generated by Django 2.0.13 on 2019-06-27 10:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 27, 10, 31, 25, 210700, tzinfo=utc), verbose_name='作成日'),
        ),
    ]
