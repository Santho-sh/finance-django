# Generated by Django 4.1.6 on 2023-02-08 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stocks',
            name='name',
            field=models.CharField(default='apple', max_length=25),
            preserve_default=False,
        ),
    ]
