# Generated by Django 4.0.1 on 2022-01-15 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_article_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
