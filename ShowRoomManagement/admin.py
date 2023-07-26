from django.contrib import admin
from . import models
# Register your models here.
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name','get_members')
    def get_members(self,obj):
        role_owners = ", ".join(profile.name for profile in obj.members.all())
        return role_owners
    get_members.short_description = "Members having this Role"
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('name','get_cars')
    list_filter = ("cars",)
    def get_cars(self,obj):
        total_cars = ", ".join(car.name for car in obj.cars.all())
        return total_cars
    get_cars.short_description = "Cars having this Role"
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name','id','brand','price','get_engine','get_showrooms','get_features')
    list_filter = ('engine',"showrooms","brand","features")
    list_per_page = 15
    def get_showrooms(self,obj):
        total_showrooms = ", ".join([showroom.name for showroom in obj.showrooms.all()])
        return total_showrooms
    def get_features(self,obj):
        total_features = ", ".join([feature.name for feature in obj.features.all()])
        return total_features
    def get_engine(self,obj):
        current_engine = obj.engine.name
        return current_engine
    get_showrooms.short_description = "Currently Avaliable In"
    get_features.short_description = "Features"
    get_engine.short_description = "Engine"
class EngineAdmin(admin.ModelAdmin):
    list_display = ("name","brand","get_Cars","get_features")
    list_filter = ("features","brand")
    list_per_page = 15
    def get_Cars(self,obj):
        carname = obj.car.name
        return carname
    def get_features(self,obj):
        features = ", ".join([feature.name for feature in obj.features.all()])
        return features
    get_Cars.short_description = "Car"
    get_features.short_description = "Features"
class BrandAdmin(admin.ModelAdmin):
    list_display = ("name","id","email","get_Total_Cars","get_Brand_Cars")
    def get_Brand_Cars(self,obj):
        cars = ", ".join([car.name for car in obj.cars.all()])
        return cars
    def get_Total_Cars(self,obj):
        total_cars = len(obj.cars.all())
        return total_cars
    get_Brand_Cars.short_description = "Cars"
    get_Total_Cars.short_description = "Total Cars"

class ShowRoomAdmin(admin.ModelAdmin):
    list_display = ("name","location","get_members","get_cars")
    list_filter = ("cars",)
    def get_members(self,obj):
        total_members = ", ".join([member.name for member in obj.members.all()])
        return total_members
    def get_cars(self,obj):
        total_cars = ", ".join(car.name for car in obj.cars.all())
        return total_cars
    get_members.short_description = "Members"
    get_cars.short_description = "Cars"
class MemberAdmin(admin.ModelAdmin):
    list_display = ("name","email","age","date_of_birth","get_showroom","role")
    list_filter = ("Current_ShowRoom","role")
    list_per_page = 15
    def get_showroom(self,obj):
        current_ShowRoom = obj.Current_ShowRoom.name
        return current_ShowRoom
    get_showroom.short_description = "Work At"
class EngineFeatureAdmin(admin.ModelAdmin):
    list_display = ("name","get_engines")
    list_filter = ("engines",)
    def get_engines(self,obj):
        engines = ", ".join([engine.name for engine in obj.engines.all()])
        return engines
    get_engines.short_description = "Engines"
admin.site.register(models.ShowRoom,ShowRoomAdmin)
admin.site.register(models.Role,RoleAdmin)
admin.site.register(models.Member,MemberAdmin)
admin.site.register(models.Brand,BrandAdmin)
admin.site.register(models.CarModel,CarModelAdmin)
admin.site.register(models.Feature,FeatureAdmin)
admin.site.register(models.Engine,EngineAdmin)
admin.site.register(models.EngineFeature,EngineFeatureAdmin)