# Generated by Django 3.2.13 on 2022-06-10 00:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_posts_hora'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='hora',
        ),
    ]
