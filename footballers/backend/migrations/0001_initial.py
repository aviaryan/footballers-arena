# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-18 07:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Footballer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=25)),
                ('nationality', models.CharField(default=None, max_length=19)),
                ('national_position', models.CharField(default=None, max_length=3)),
                ('national_kit', models.CharField(default=None, max_length=2)),
                ('club', models.CharField(default=None, max_length=17)),
                ('club_position', models.CharField(default=None, max_length=3)),
                ('club_kit', models.CharField(default=None, max_length=2)),
                ('club_joining', models.CharField(default=None, max_length=10)),
                ('contract_expiry', models.CharField(default=None, max_length=4)),
                ('rating', models.IntegerField(default=None)),
                ('height', models.CharField(default=None, max_length=6)),
                ('weight', models.CharField(default=None, max_length=5)),
                ('preffered_foot', models.CharField(default=None, max_length=5)),
                ('birth_date', models.CharField(default=None, max_length=10)),
                ('age', models.IntegerField(default=None)),
                ('preffered_position', models.CharField(default=None, max_length=9)),
                ('work_rate', models.CharField(default=None, max_length=15)),
                ('weak_foot', models.IntegerField(default=None)),
                ('skill_moves', models.IntegerField(default=None)),
                ('ball_control', models.IntegerField(default=None)),
                ('dribbling', models.IntegerField(default=None)),
                ('marking', models.IntegerField(default=None)),
                ('sliding_tackle', models.IntegerField(default=None)),
                ('standing_tackle', models.IntegerField(default=None)),
                ('aggression', models.IntegerField(default=None)),
                ('reactions', models.IntegerField(default=None)),
                ('attacking_position', models.IntegerField(default=None)),
                ('interceptions', models.IntegerField(default=None)),
                ('vision', models.IntegerField(default=None)),
                ('composure', models.IntegerField(default=None)),
                ('crossing', models.IntegerField(default=None)),
                ('short_pass', models.IntegerField(default=None)),
                ('long_pass', models.IntegerField(default=None)),
                ('acceleration', models.IntegerField(default=None)),
                ('speed', models.IntegerField(default=None)),
                ('stamina', models.IntegerField(default=None)),
                ('strength', models.IntegerField(default=None)),
                ('balance', models.IntegerField(default=None)),
                ('agility', models.IntegerField(default=None)),
                ('jumping', models.IntegerField(default=None)),
                ('heading', models.IntegerField(default=None)),
                ('shot_power', models.IntegerField(default=None)),
                ('finishing', models.IntegerField(default=None)),
                ('long_shots', models.IntegerField(default=None)),
                ('curve', models.IntegerField(default=None)),
                ('freekick_accuracy', models.IntegerField(default=None)),
                ('penalties', models.IntegerField(default=None)),
                ('volleys', models.IntegerField(default=None)),
                ('gk_positioning', models.IntegerField(default=None)),
                ('gk_diving', models.IntegerField(default=None)),
                ('gk_kicking', models.IntegerField(default=None)),
                ('gk_handling', models.IntegerField(default=None)),
                ('gk_reflexes', models.IntegerField(default=None)),
            ],
        ),
    ]
