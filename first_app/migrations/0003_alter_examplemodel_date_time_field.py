# Generated by Django 5.0.3 on 2024-04-27 04:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_examplemodel_boolean_field_examplemodel_char_field_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examplemodel',
            name='date_time_field',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 27, 4, 0, 42, 825566)),
        ),
    ]
