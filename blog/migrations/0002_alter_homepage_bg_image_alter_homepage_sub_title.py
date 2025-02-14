# Generated by Django 5.1.4 on 2025-01-04 19:01

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='bg_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/', validators=[blog.models.validate_image_dimensions]),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='sub_title',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
