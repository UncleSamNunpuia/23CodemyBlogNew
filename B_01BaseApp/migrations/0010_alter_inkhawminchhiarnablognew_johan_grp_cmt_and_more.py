# Generated by Django 4.2.1 on 2023-05-09 11:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('B_01BaseApp', '0009_alter_inkhawminchhiarnablognew_leader_secy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inkhawminchhiarnablognew',
            name='johan_grp_cmt',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(25)]),
        ),
        migrations.AlterField(
            model_name='inkhawminchhiarnablognew',
            name='luka_grp_cmt',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(25)]),
        ),
        migrations.AlterField(
            model_name='inkhawminchhiarnablognew',
            name='marka_grp_cmt',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(25)]),
        ),
        migrations.AlterField(
            model_name='inkhawminchhiarnablognew',
            name='mat_grp_cmt',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(25)]),
        ),
    ]