# Generated by Django 2.2.5 on 2019-09-26 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0003_bbs_bbshot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bbs',
            name='bbshot',
            field=models.IntegerField(default=0, verbose_name='是否为精华帖'),
        ),
    ]
