# Generated by Django 3.0.5 on 2020-05-29 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontpage', '0009_exame_audiorecorded'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exame',
            name='audioRecorded',
            field=models.FileField(blank=True, upload_to='media/'),
        ),
    ]
