# Generated by Django 3.1.7 on 2021-04-18 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0013_auto_20210414_2035'),
    ]

    operations = [
        migrations.AddField(
            model_name='internshipapplieddb',
            name='certificate',
            field=models.ImageField(blank=True, null=True, upload_to='student/certificate/'),
        ),
    ]
