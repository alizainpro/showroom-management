# Generated by Django 4.1.2 on 2023-07-25 03:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ShowRoomManagement', '0015_alter_carmodel_engine'),
    ]

    operations = [
        migrations.CreateModel(
            name='EngineFeature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=700, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='engine',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='engines', to='ShowRoomManagement.brand'),
        ),
        migrations.AddField(
            model_name='engine',
            name='engine_pic',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='engine',
            name='features',
            field=models.ManyToManyField(null=True, related_name='engines', to='ShowRoomManagement.enginefeature'),
        ),
    ]
