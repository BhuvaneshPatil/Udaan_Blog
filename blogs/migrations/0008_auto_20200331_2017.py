# Generated by Django 2.2.5 on 2020-03-31 14:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0007_auto_20200331_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 31, 14, 47, 14, 954492, tzinfo=utc)),
        ),
    ]
