# Generated by Django 3.1.3 on 2021-02-26 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metro', '0003_auto_20210227_0055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='station',
            name='description',
            field=models.TextField(blank=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='station',
            name='image',
            field=models.ImageField(blank=True, upload_to='stations_photos', verbose_name='Classic Photo'),
        ),
        migrations.AlterField(
            model_name='station',
            name='instagram_url',
            field=models.SlugField(blank=True, max_length=150),
        ),
    ]