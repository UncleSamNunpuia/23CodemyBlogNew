# Generated by Django 4.2 on 2023-04-14 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('A_theBlogNew', '0007_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
