# Generated by Django 4.2.5 on 2023-09-25 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_story'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('background', models.ImageField(upload_to='', verbose_name='Background')),
                ('img', models.ImageField(upload_to='', verbose_name='Image')),
                ('url', models.URLField(verbose_name='Video Url')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('text1', models.TextField(verbose_name='Text 1')),
                ('text2', models.TextField(verbose_name='Text 2')),
            ],
            options={
                'verbose_name': 'About',
                'verbose_name_plural': 'About',
            },
        ),
    ]