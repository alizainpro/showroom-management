# Generated by Django 4.1.2 on 2023-07-24 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShowRoomManagement', '0004_remove_brand_cars_brand_cars'),
    ]

    operations = [
        migrations.AddField(
            model_name='showroom',
            name='showroom_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]