from django.urls import path, re_path
from . import views

urlpatterns = [
    path('create_ad_connection/', views.CreateADConn.as_view(), name='create_ad_connection'),
    path('get_users/', views.GetADUsers.as_view(), name='get_users'),
]
