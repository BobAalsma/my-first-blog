# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('klanten', '0002_remove_klant_published_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='klant',
            name='verantwoordelijke',
            field=models.CharField(default=b'Joop', max_length=200, verbose_name=b'verantwoordelijke'),
        ),
        migrations.AddField(
            model_name='klant',
            name='woonplaats',
            field=models.CharField(default=b'Utercht', max_length=200, verbose_name=b'woomplaats'),
        ),
        migrations.AlterField(
            model_name='klant',
            name='naam',
            field=models.CharField(max_length=200, verbose_name=b'organisatie'),
        ),
    ]
