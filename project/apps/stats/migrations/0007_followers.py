# Generated by Django 4.1.5 on 2023-08-10 10:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stats', '0006_alter_articlecomments_article_comments_article_id_fk_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Followers',
            fields=[
                ('follower_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('change', models.IntegerField(default=0)),
                ('count', models.IntegerField(default=0)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('article_user_id_fk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
