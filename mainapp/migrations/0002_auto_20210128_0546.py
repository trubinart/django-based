# Generated by Django 3.1.5 on 2021-01-28 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='description',
            field=models.TextField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='products',
            name='short_description',
            field=models.TextField(max_length=256),
        ),
    ]
