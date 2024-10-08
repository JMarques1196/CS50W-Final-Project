# Generated by Django 5.0.2 on 2024-09-06 09:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('final', '0006_remove_media_url_media_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='url',
        ),
        migrations.AddField(
            model_name='media',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='link', to='final.project'),
        ),
        migrations.AlterField(
            model_name='media',
            name='url',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
