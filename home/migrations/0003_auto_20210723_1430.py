# Generated by Django 3.2.5 on 2021-07-23 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_blog_featured_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='view',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='page',
            name='view',
            field=models.IntegerField(default=0),
        ),
    ]
