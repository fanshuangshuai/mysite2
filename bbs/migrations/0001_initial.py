# Generated by Django 2.2.5 on 2019-09-26 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('boardid', models.AutoField(primary_key=True, serialize=False, verbose_name='板块自动编号')),
                ('boardname', models.CharField(max_length=200, verbose_name='版块名称')),
                ('boardtopics', models.IntegerField(default=0, verbose_name='版块主题数')),
                ('boardmanager', models.CharField(max_length=200, verbose_name='版主名')),
                ('boardintroduce', models.CharField(default='', max_length=200, verbose_name='板块介绍')),
            ],
            options={
                'db_table': 'Board',
            },
        ),
        migrations.CreateModel(
            name='Bbs',
            fields=[
                ('bbsid', models.AutoField(primary_key=True, serialize=False, verbose_name='帖子自动编号')),
                ('parentid', models.IntegerField(default=None, verbose_name='父贴编号')),
                ('child', models.IntegerField(default=None, verbose_name='跟帖数')),
                ('username', models.CharField(max_length=100, verbose_name='发表人姓名')),
                ('expression', models.CharField(max_length=100, verbose_name='发帖人E-mail')),
                ('bbstitle', models.CharField(max_length=200, verbose_name='发表人标题')),
                ('bbscontent', models.TextField(verbose_name='文章内容')),
                ('dateandtime', models.DateTimeField(verbose_name='文章发表时间')),
                ('bbsclick', models.IntegerField(default=0, verbose_name='论坛点击率')),
                ('bbshot', models.BinaryField(default=0, verbose_name='是否为精华帖')),
                ('boardid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bbs.Board')),
            ],
            options={
                'db_table': 'Bbs',
            },
        ),
    ]