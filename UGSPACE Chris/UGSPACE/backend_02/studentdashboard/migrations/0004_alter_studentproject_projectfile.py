# Generated by Django 4.0.3 on 2022-04-16 03:17

from django.db import migrations, models
import studentdashboard.models


class Migration(migrations.Migration):

    dependencies = [
        ('studentdashboard', '0003_alter_studentproject_projectfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentproject',
            name='projectfile',
            field=models.FileField(default=0, upload_to=studentdashboard.models.content_file_name),
        ),
    ]
