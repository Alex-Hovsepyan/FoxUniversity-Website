# Generated by Django 4.2.5 on 2023-09-25 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_offercontent_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='header',
            name='subheader_background',
            field=models.ImageField(default=1, upload_to='', verbose_name='SubHeader Background'),
            preserve_default=False,
        ),
    ]