# Generated by Django 2.2.5 on 2019-10-02 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190929_2030'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThemeBlog',
            fields=[
                ('blog_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blog.Blog')),
                ('theme', models.CharField(max_length=200)),
            ],
            bases=('blog.blog',),
        ),
    ]
