# Generated by Django 4.1.4 on 2023-05-10 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faqs',
            name='image',
        ),
        migrations.AddField(
            model_name='faqs',
            name='description',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]
