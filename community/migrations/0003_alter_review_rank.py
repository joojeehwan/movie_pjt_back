# Generated by Django 3.2.3 on 2021-11-23 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0002_review_rank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rank',
            field=models.IntegerField(default=0),
        ),
    ]
