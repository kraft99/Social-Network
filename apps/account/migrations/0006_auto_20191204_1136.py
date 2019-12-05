# Generated by Django 2.2.6 on 2019-12-04 19:36

import apps.common.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20191125_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='pic',
            field=models.ImageField(blank=True, default=apps.common.utils.default_avatar_url, null=True, upload_to=apps.common.utils.profile_dp),
        ),
    ]
