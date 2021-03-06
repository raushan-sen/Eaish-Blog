# Generated by Django 3.2.5 on 2021-07-24 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20210724_0258'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='Comment',
            new_name='comment',
        ),
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.SlugField(blank=True, default=None, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='thumbnail',
            field=models.ImageField(blank=True, default='/static/images/default.jpg', null=True, upload_to='static/images'),
        ),
        migrations.AlterField(
            model_name='categery',
            name='slug',
            field=models.SlugField(blank=True, default=None, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='comment',
            name='slug',
            field=models.SlugField(blank=True, default=None, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='slug',
            field=models.SlugField(blank=True, default=None, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='thumbnail',
            field=models.ImageField(blank=True, default='/static/images/default.jpg', null=True, upload_to='static/images'),
        ),
    ]
