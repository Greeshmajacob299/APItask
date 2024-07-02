# Generated by Django 5.0.6 on 2024-07-02 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='google_map_link',
            field=models.URLField(default=1234),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='destination',
            name='dest_image',
            field=models.ImageField(upload_to='tourist_dest/'),
        ),
    ]