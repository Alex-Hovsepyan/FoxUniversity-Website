# Generated by Django 4.2.5 on 2023-09-25 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(verbose_name='Count')),
                ('title', models.CharField(max_length=40, verbose_name='Title')),
            ],
        ),
    ]