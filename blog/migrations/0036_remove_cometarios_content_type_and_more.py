# Generated by Django 4.1.3 on 2022-11-19 21:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0035_alter_cometarios_options_remove_cometarios_post_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cometarios',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='cometarios',
            name='object_id',
        ),
        migrations.AddField(
            model_name='cometarios',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.postblog'),
        ),
    ]
