# Generated by Django 4.2 on 2023-04-10 11:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('A_theBlogNew', '0005_alter_post_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='images/'),
            preserve_default=False,
        ),
    ]