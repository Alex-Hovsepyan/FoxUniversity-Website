# Generated by Django 4.2.5 on 2023-09-26 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_courses_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courses',
            name='slug',
        ),
    ]
