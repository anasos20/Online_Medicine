# Generated by Django 4.0.7 on 2022-09-11 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newss', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='thumb',
            field=models.ImageField(blank=True, default='about-medicine.png', null=True, upload_to=''),
        ),
    ]
