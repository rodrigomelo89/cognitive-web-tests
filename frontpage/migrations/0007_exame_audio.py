# Generated by Django 3.0.5 on 2020-05-20 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontpage', '0006_auto_20200519_1222'),
    ]

    operations = [
        migrations.AddField(
            model_name='exame',
            name='audio',
            field=models.FilePathField(default=''),
        ),
    ]