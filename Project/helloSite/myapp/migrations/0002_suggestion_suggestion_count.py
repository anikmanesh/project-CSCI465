# Generated by Django 2.1.7 on 2019-03-05 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='suggestion',
            name='suggestion_count',
            field=models.IntegerField(default=0),
        ),
    ]