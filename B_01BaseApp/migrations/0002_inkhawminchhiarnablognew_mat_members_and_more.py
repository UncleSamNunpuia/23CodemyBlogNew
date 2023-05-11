# Generated by Django 4.2 on 2023-04-18 08:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('B_01BaseApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='inkhawminchhiarnablognew',
            name='mat_members',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(300)]),
        ),
        migrations.AlterField(
            model_name='inkhawminchhiarnablognew',
            name='mat_grp_cmt',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(24)]),
        ),
    ]
