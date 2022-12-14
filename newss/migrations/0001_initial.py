# Generated by Django 4.0.7 on 2022-09-10 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('body', models.TextField()),
                ('thumb', models.ImageField(blank=True, default='images/about-medicine.png', null=True, upload_to='')),
            ],
        ),
    ]
