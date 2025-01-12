# Generated by Django 3.2.8 on 2023-01-30 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'post_category',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('content', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('owner_article', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'comment',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('subhead', models.TextField(default=None, max_length=100)),
                ('body', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('owner_id', models.IntegerField(default=0)),
                ('cate_id', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'post',
            },
        ),
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.CharField(default=None, max_length=10000)),
                ('name', models.CharField(default=None, max_length=100)),
                ('link', models.CharField(default=None, max_length=100)),
            ],
            options={
                'db_table': 'post_image',
            },
        ),
        migrations.CreateModel(
            name='Verse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('author', models.CharField(blank=True, max_length=50, null=True)),
                ('create_time', models.DateField(auto_now_add=True)),
                ('cate_id', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'verse',
            },
        ),
        migrations.CreateModel(
            name='VerseCate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'verse_cate',
            },
        ),
    ]