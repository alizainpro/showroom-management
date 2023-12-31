# Generated by Django 4.1.2 on 2023-07-25 01:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ShowRoomManagement', '0009_carmodel_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Engine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=700)),
            ],
        ),
        migrations.AddField(
            model_name='carmodel',
            name='engine',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='ShowRoomManagement.engine'),
        ),
    ]
