# Generated by Django 4.2.7 on 2023-11-16 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0002_compressedimage_delete_imagemodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compressedimage',
            name='compressed_image',
        ),
    ]