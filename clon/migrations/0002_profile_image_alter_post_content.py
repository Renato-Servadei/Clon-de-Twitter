# Generated by Django 4.2.1 on 2023-05-20 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clon', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.png', upload_to=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(),
        ),
    ]
