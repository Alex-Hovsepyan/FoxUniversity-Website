# Generated by Django 4.2.5 on 2023-09-25 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_aboutcontent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='', verbose_name='Image')),
                ('url', models.URLField(verbose_name='Image Url')),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='', verbose_name='Image')),
                ('text', models.TextField(verbose_name='Text')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('position', models.CharField(max_length=50, verbose_name='Position')),
            ],
        ),
        migrations.CreateModel(
            name='TestimonialTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('text1', models.TextField(verbose_name='Text 1')),
                ('text2', models.TextField(verbose_name='Text 2')),
            ],
            options={
                'verbose_name': 'Testimonial Title',
                'verbose_name_plural': 'Testimonial Title',
            },
        ),
    ]
