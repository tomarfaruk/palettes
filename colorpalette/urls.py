from django.urls import path, include

from . import views

from rest_framework import routers

routs = routers.DefaultRouter()
routs.register('palettes', views.PaletteView)

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.PaletteList), 
    path('api/', include(routs.urls), name='palettes'),
    path('api/v1/auth/login', views.LoginView.as_view()),
]