# Generated by Django 4.2.4 on 2023-10-23 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_course_total_enrollment'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='admin', max_length=16),
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='admin', max_length=16),
        ),
    ]
