# Generated by Django 4.1.2 on 2023-07-25 01:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ShowRoomManagement', '0011_alter_carmodel_engine'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmodel',
            name='engine',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='ShowRoomManagement.engine'),
        ),
    ]
