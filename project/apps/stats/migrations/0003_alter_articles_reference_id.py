# Generated by Django 4.1.5 on 2023-02-21 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0002_alter_articlecomments_change_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='reference_id',
            field=models.IntegerField(),
        ),
    ]