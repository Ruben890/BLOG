# Generated by Django 4.1.3 on 2022-11-24 00:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0053_rename_user_cometarios_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cometarios',
            name='data',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
