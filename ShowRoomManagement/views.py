from django.shortcuts import render
from . import models

# Create your views here.
def index(request):
    showrooms = models.ShowRoom.objects.all()
    DATA = {'showrooms':showrooms}
    return render(request,'ShowRoomManagement/index.html',DATA)
def brands(request):
    BRANDS = models.Brand.objects.all()
    avaliable_BRANDS = []
    for brandobject in BRANDS:
        avaliable_BRANDS.append({'name':brandobject.name,'cars_length':brandobject.cars.all().__len__,'id':brandobject.id,'brand_logo':brandobject.brand_logo})
    DATA = {'brands':avaliable_BRANDS}
    return render(request,'ShowRoomManagement/brands.html',DATA)
def showroom_view(request,showroom_id):
    theshowroom = models.ShowRoom.objects.get(id=showroom_id)
    total_Cars = theshowroom.cars.all()

    # print(total_Cars[0].brand.all()[0].name)
    DATA = {'cars':total_Cars,'showroomname':theshowroom.name,'showroom':theshowroom}
    return render(request,'ShowRoomManagement/showroom.html',DATA)
def TeamView(request,showroomid):
    theshowroom = models.ShowRoom.objects.get(id=showroomid)
    total_Members = theshowroom.members.all()
    DATA = {'members':total_Members,'showroomname':theshowroom.name,'total_members':len(total_Members)}
    return render(request,'ShowRoomManagement/teamview.html',context=DATA)
def Car(request,car_id):
    current_Car = models.CarModel.objects.get(id=car_id)
    DATA = {'car':current_Car}
    return render(request,'ShowRoomManagement/car.html',DATA)
def MemberView(request,member_id):
    current_Member = models.Member.objects.get(id=member_id)
    DATA = {'member':current_Member}
    return render(request,'ShowRoomManagement/member.html',context=DATA)
def BrandView(request,brandid):
    current_brand = models.Brand.objects.get(id=brandid)
    DATA = {'brand':current_brand,'cars_length':len(current_brand.cars.all())}
    return render(request,'ShowRoomManagement/brand.html',DATA)
def EngineView(request,engineid):
    current_engine = models.Engine.objects.get(id=engineid)
    DATA = {'engine':current_engine}
    return render(request,'ShowRoomManagement/enginedetails.html',DATA)
def featurefilterindex(request):
    Features = models.Feature.objects.all()
    DATA = {'features':Features,'featurescount':len(Features)}
    return render(request,'ShowRoomManagement/featuresfilter.html',DATA)
def featurefilter(request,feature_id):
    current_Feature = models.Feature.objects.get(id=feature_id)
    cars_length = len(current_Feature.cars.all())
    DATA = {'feature':current_Feature,'cars_length':cars_length}
    return render(request,'ShowRoomManagement/featurefilter.html',DATA)
def ourteam(request):
    showrooms = models.ShowRoom.objects.all()
    DATA = {'showrooms':showrooms}
    return render(request,'ShowRoomManagement/ourteam.html',DATA)