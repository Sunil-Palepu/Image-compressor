# Generated by Django 4.2.7 on 2023-11-16 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompressedImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_image', models.ImageField(upload_to='original_images/')),
                ('compressed_image', models.ImageField(blank=True, null=True, upload_to='compressed_images/')),
            ],
        ),
        migrations.DeleteModel(
            name='ImageModel',
        ),
    ]