# Generated by Django 4.1.3 on 2022-11-19 22:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0037_rename_post_cometarios_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cometarios',
            old_name='title',
            new_name='post',
        ),
    ]
