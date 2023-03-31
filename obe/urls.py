from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'obe'

urlpatterns = [
    path('matkul/', MatkulPageView.as_view(), name="matkul"),
    path('matkul-pengukur/', MatkulPengukurPageView.as_view(), name="matkul_pengukur"),
    path('matkul-pengukur/detail/<int:pk>/', DetailMatkulPengukurPageView.as_view(), name="detail_matkul_pengukur"),
    path('matkul/create/', CreateMatkulPageView.as_view(), name="create_matkul"),
    path('matkul/update/<int:pk>/', UpdateMatkulPageView.as_view(), name="update_matkul"),
]