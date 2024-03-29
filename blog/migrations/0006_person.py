# Generated by Django 2.2.5 on 2019-10-07 14:31

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_author_blog_entry_themeblog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('role', models.CharField(choices=[('A', 'Author'), ('E', 'Editor')], max_length=1)),
            ],
            managers=[
                ('people', django.db.models.manager.Manager()),
            ],
        ),
    ]
