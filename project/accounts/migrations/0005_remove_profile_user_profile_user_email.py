# Generated by Django 4.1.3 on 2022-12-26 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_profile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.AddField(
            model_name='profile',
            name='user_email',
            field=models.EmailField(blank=True, max_length=255),
        ),
    ]
