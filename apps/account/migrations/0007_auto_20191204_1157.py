# Generated by Django 2.2.6 on 2019-12-04 19:57

import apps.common.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20191204_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to=apps.common.utils.profile_dp),
        ),
    ]
