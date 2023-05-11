# Generated by Django 4.2 on 2023-04-20 08:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('B_01BaseApp', '0007_alter_inkhawminchhiarnablognew_marka_grp_cmt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inkhawminchhiarnablognew',
            name='johan_grp_cmt',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(24)]),
        ),
        migrations.AlterField(
            model_name='inkhawminchhiarnablognew',
            name='johan_members',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(300)]),
        ),
        migrations.AlterField(
            model_name='inkhawminchhiarnablognew',
            name='luka_grp_cmt',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(24)]),
        ),
        migrations.AlterField(
            model_name='inkhawminchhiarnablognew',
            name='luka_members',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(300)]),
        ),
        migrations.AlterField(
            model_name='inkhawminchhiarnablognew',
            name='marka_members',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(300)]),
        ),
    ]