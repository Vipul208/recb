# Generated by Django 4.1.4 on 2023-05-10 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_rename_heading_noticeboard_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallerie',
            name='title',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lslider',
            name='title',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
