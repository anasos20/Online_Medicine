# Generated by Django 4.0.7 on 2022-09-11 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('price', models.PositiveIntegerField()),
                ('date_added', models.DateField(auto_now_add=True)),
                ('thumb', models.ImageField(blank=True, default='p-6', null=True, upload_to='')),
            ],
        ),
    ]