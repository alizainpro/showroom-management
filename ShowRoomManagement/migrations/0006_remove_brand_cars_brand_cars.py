# Generated by Django 4.1.2 on 2023-07-24 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ShowRoomManagement', '0005_showroom_showroom_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='cars',
        ),
        migrations.AddField(
            model_name='brand',
            name='cars',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='brand', to='ShowRoomManagement.carmodel'),
        ),
    ]
