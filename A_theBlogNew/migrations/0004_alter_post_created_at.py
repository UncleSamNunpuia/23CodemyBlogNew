# Generated by Django 4.1.7 on 2023-04-02 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('A_theBlogNew', '0003_alter_post_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(),
        ),
    ]