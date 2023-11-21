# Generated by Django 4.2.7 on 2023-11-21 06:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('tmdb_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('poster_path', models.CharField(max_length=255)),
                ('tmdb_id', models.IntegerField()),
                ('movie_rate', models.FloatField()),
                ('release_date', models.CharField(max_length=50)),
                ('action', models.BooleanField(default=False)),
                ('adventure', models.BooleanField(default=False)),
                ('animation', models.BooleanField(default=False)),
                ('comedy', models.BooleanField(default=False)),
                ('crime', models.BooleanField(default=False)),
                ('documentary', models.BooleanField(default=False)),
                ('drama', models.BooleanField(default=False)),
                ('family', models.BooleanField(default=False)),
                ('fantasy', models.BooleanField(default=False)),
                ('history', models.BooleanField(default=False)),
                ('horror', models.BooleanField(default=False)),
                ('music', models.BooleanField(default=False)),
                ('mystery', models.BooleanField(default=False)),
                ('romance', models.BooleanField(default=False)),
                ('science_fiction', models.BooleanField(default=False)),
                ('tv_movie', models.BooleanField(default=False)),
                ('thriller', models.BooleanField(default=False)),
                ('war', models.BooleanField(default=False)),
                ('western', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='UserImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, upload_to='images/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserGenre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.IntegerField(default=0)),
                ('adventure', models.IntegerField(default=0)),
                ('animation', models.IntegerField(default=0)),
                ('comedy', models.IntegerField(default=0)),
                ('crime', models.IntegerField(default=0)),
                ('documentary', models.IntegerField(default=0)),
                ('drama', models.IntegerField(default=0)),
                ('family', models.IntegerField(default=0)),
                ('fantasy', models.IntegerField(default=0)),
                ('history', models.IntegerField(default=0)),
                ('horror', models.IntegerField(default=0)),
                ('music', models.IntegerField(default=0)),
                ('mystery', models.IntegerField(default=0)),
                ('romance', models.IntegerField(default=0)),
                ('science_fiction', models.IntegerField(default=0)),
                ('tv_movie', models.IntegerField(default=0)),
                ('thriller', models.IntegerField(default=0)),
                ('war', models.IntegerField(default=0)),
                ('western', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MovieGenre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
