# Generated by Django 5.0.2 on 2024-09-06 09:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('final', '0007_remove_project_url_media_project_alter_media_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='media',
            name='project',
        ),
        migrations.AddField(
            model_name='project',
            name='media',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='link', to='final.media'),
        ),
    ]
