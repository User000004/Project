# Generated by Django 3.2.14 on 2022-07-14 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0021_alter_experiment_time_after_experiment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videorecording',
            name='video_duration',
            field=models.IntegerField(null=True),
        ),
    ]
