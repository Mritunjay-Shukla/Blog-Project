# Generated by Django 2.2.5 on 2020-06-20 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_post_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='date',
        ),
    ]
