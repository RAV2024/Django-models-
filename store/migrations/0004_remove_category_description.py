# Generated by Django 4.2.16 on 2024-10-22 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_remove_brand_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='description',
        ),
    ]
