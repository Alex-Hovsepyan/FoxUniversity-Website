# Generated by Django 4.2.5 on 2023-09-26 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_courses'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='slug',
            field=models.SlugField(default=1, unique=True, verbose_name='Slug'),
            preserve_default=False,
        ),
    ]
