# Generated by Django 3.2 on 2021-04-30 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='moneys',
            field=models.DecimalField(decimal_places=2, default=1000, max_digits=6),
        ),
    ]