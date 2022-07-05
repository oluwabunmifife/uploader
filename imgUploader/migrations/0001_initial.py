# Generated by Django 4.0.3 on 2022-07-05 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(blank=True, height_field=100, null=True, upload_to='', width_field=100)),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(help_text='Give a short description of the image', max_length=100)),
            ],
        ),
    ]
