# Generated by Django 2.2 on 2021-06-11 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://foodlocate.com/assets/img/tmp/placeholder_restaurant.jpg', max_length=500),
        ),
    ]