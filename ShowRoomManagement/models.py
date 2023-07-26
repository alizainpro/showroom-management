from django.db import models

from django.core.files.storage import FileSystemStorage
from django.conf import settings

fs = FileSystemStorage(settings.MEDIA_ROOT,settings.MEDIA_URL)
# Create your models here.
class Role(models.Model):
    name = models.CharField(max_length=400,unique=True)
    def __str__(self) -> str:
        return self.name
class Feature(models.Model):
    name = models.CharField(max_length=700,unique=True)
    def __str__(self) -> str:
        return self.name
class EngineFeature(models.Model):
    name = models.CharField(max_length=700,unique=True)
    def __str__(self) -> str:
        return self.name
class Brand(models.Model):
    name = models.CharField(max_length=250,unique=True)
    brand_logo = models.ImageField(null=True,blank=True)
    email = models.EmailField(unique=True,max_length=265)
    def __str__(self) -> str:
        return self.name
class Engine(models.Model):
    name = models.CharField(max_length=700)
    engine_pic = models.ImageField(null=True)
    features = models.ManyToManyField(EngineFeature,related_name="engines",null=True)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE,related_name="engines",null=True)
    def __str__(self) -> str:
        return self.name
class CarModel(models.Model):
    name = models.CharField(max_length=400,unique=True)
    car_image = models.ImageField()
    price = models.IntegerField(default=200)
    features = models.ManyToManyField(Feature,related_name="cars")
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE,related_name="cars",null=True)
    engine = models.OneToOneField(Engine,on_delete=models.CASCADE,related_name="car",null=True)
    def __str__(self) -> str:
        return self.name
class ShowRoom(models.Model):
    name = models.CharField(max_length=300)
    location = models.CharField(max_length=350)
    showroom_image = models.ImageField(null=True,blank=True)
    cars = models.ManyToManyField(CarModel,related_name="showrooms")
    def __str__(self) -> str:
        return self.name
class Member(models.Model):
    name = models.CharField(max_length=400)
    email = models.EmailField(max_length=500,unique=True)
    age = models.IntegerField()
    profile_pic = models.ImageField(null=True,blank=True)
    date_of_birth = models.DateField(null=True)
    Current_ShowRoom = models.ForeignKey(ShowRoom,on_delete=models.CASCADE,related_name='members',null=True)
    role = models.ForeignKey(Role,on_delete=models.CASCADE,related_name="members")
    def __str__(self) -> str:
        return self.name
    

