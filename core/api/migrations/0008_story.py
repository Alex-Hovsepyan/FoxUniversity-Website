# Generated by Django 4.2.5 on 2023-09-25 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_header_subheader_background'),
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subheader_title', models.CharField(max_length=40, verbose_name='SubHeader Title')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('text1', models.TextField(verbose_name='Text1')),
                ('text2', models.TextField(verbose_name='Text2')),
                ('text3', models.TextField(verbose_name='Text3')),
                ('img', models.ImageField(upload_to='', verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Story',
                'verbose_name_plural': 'Story',
            },
        ),
    ]
