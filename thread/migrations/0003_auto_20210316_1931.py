# Generated by Django 3.1.7 on 2021-03-17 02:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thread', '0002_comment_dislikes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gamethread',
            options={'ordering': ['-date']},
        ),
    ]