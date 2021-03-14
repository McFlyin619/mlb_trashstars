# Generated by Django 3.1.7 on 2021-03-14 08:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('thread', '0003_delete_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='likes',
            field=models.ManyToManyField(related_name='comment_like', to=settings.AUTH_USER_MODEL),
        ),
    ]