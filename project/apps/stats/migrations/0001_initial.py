# Generated by Django 4.1.5 on 2023-02-16 13:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('tag_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.TextField(max_length=50)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('article_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('reference_id', models.TextField(max_length=50)),
                ('title', models.TextField(max_length=200)),
                ('is_published', models.BooleanField()),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('url', models.URLField(blank=True, max_length=1000, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('article_user_id_fk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('tags', models.ManyToManyField(blank=True, to='stats.tags')),
            ],
        ),
        migrations.CreateModel(
            name='ArticleLikes',
            fields=[
                ('article_likes_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('change', models.IntegerField()),
                ('count', models.IntegerField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('article_likes_article_id_fk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ArticleComments',
            fields=[
                ('article_comments_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('change', models.IntegerField()),
                ('count', models.IntegerField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('article_comments_article_id_fk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]