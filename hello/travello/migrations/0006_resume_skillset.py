# Generated by Django 4.1.4 on 2022-12-31 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0005_resume_delete_upload'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='skillset',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
