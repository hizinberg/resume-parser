# Generated by Django 4.1.4 on 2022-12-20 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0002_rename_headline_todo_todo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('venu_image', models.ImageField(blank=True, null=True, upload_to='images')),
            ],
        ),
        migrations.DeleteModel(
            name='Todo',
        ),
    ]
