# Generated by Django 4.1.2 on 2023-07-25 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShowRoomManagement', '0007_remove_brand_cars_carmodel_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmodel',
            name='features',
            field=models.ManyToManyField(related_name='cars', to='ShowRoomManagement.feature'),
        ),
    ]
