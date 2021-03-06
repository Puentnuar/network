# Generated by Django 3.1.4 on 2020-12-26 10:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0008_remove_follow_following_posts'),
    ]

    operations = [
        migrations.AddField(
            model_name='follow',
            name='following_posts',
            field=models.ManyToManyField(default=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following_user', to=settings.AUTH_USER_MODEL), to='network.Post'),
        ),
    ]
