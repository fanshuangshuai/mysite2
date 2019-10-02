# Generated by Django 2.2.5 on 2019-10-02 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_themeblog'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='authors',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='blog',
        ),
        migrations.RemoveField(
            model_name='themeblog',
            name='blog_ptr',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
        migrations.DeleteModel(
            name='Entry',
        ),
        migrations.DeleteModel(
            name='ThemeBlog',
        ),
    ]
