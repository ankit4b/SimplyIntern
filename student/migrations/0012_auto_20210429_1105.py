# Generated by Django 3.1.7 on 2021-04-29 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0011_auto_20210426_1841'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='auth_token',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AddField(
            model_name='student',
            name='isVerified',
            field=models.BooleanField(default=False),
        ),
    ]