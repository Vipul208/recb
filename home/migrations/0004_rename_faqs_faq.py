# Generated by Django 4.1.4 on 2023-05-10 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_rename_description_faqs_answer_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='faqs',
            new_name='faq',
        ),
    ]
