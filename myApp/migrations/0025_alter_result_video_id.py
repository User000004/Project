# Generated by Django 3.2.14 on 2022-07-14 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0024_alter_videorecording_video_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='video_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.videorecording'),
        ),
    ]
