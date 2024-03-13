# Generated by Django 5.0.3 on 2024-03-13 13:53

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spottiapp', '0005_post_post_date'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(related_name='blog_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]