# Generated by Django 5.0.2 on 2024-09-20 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('final', '0015_rename_comment_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='link',
            field=models.CharField(default='placeholder', max_length=200),
            preserve_default=False,
        ),
    ]
