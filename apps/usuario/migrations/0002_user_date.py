# Generated by Django 3.1.1 on 2020-09-07 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='date',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
