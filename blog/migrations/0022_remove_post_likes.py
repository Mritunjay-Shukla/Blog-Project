# Generated by Django 2.2.5 on 2020-06-27 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_post_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
    ]