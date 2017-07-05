# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-04 09:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0002_auto_20170704_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='cc',
            field=models.IntegerField(default=49, help_text='Country code without +'),
        ),
        migrations.AlterField(
            model_name='account',
            name='phone',
            field=models.BigIntegerField(help_text='Full phone number with country code but without +', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='message',
            name='origin',
            field=models.BigIntegerField(help_text='Phone number of WhatsApp account owner'),
        ),
        migrations.AlterField(
            model_name='message',
            name='target',
            field=models.BigIntegerField(help_text='Full phone number of recepiant with country code but without +'),
        ),
    ]