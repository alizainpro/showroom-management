"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

app_name = "ShowRoomManagement"
urlpatterns = [
    path('',views.index,name="Index"),
    path('brands/',views.brands,name="Brands"),
    path('showroom/<int:showroom_id>',views.showroom_view,name="ShowRoom"),
    path('car/<int:car_id>',views.Car,name="Car"),
    path('member/<int:member_id>',views.MemberView,name="Member"),
    path('team/<int:showroomid>',views.TeamView,name="TeamView"),
    path('brands/<int:brandid>',views.BrandView,name="BrandView"),
    path('featuresfilter/',views.featurefilterindex,name="featuresfilter"),
    path('featurefilter/<int:feature_id>',views.featurefilter,name="featurefilter"),
    path('engineview/<int:engineid>',views.EngineView,name="EngineView"),
    path("teams/",views.ourteam,name="ViewTeams")

]
