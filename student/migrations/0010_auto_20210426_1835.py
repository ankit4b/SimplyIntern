# Generated by Django 3.1.7 on 2021-04-26 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0009_certificate_credential'),
    ]

    operations = [
        migrations.RenameField(
            model_name='certificate',
            old_name='resume_file',
            new_name='certificate_file',
        ),
    ]