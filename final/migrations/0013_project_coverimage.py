# Generated by Django 5.0.2 on 2024-09-09 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('final', '0012_media_resourcetitle'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='coverImage',
            field=models.CharField(default='placeholder', max_length=500),
            preserve_default=False,
        ),
    ]
