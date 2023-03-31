from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'akun'

urlpatterns = [
    path('daftar/', daftar, name="daftar"),
    path('login/', login, name="login"),
    path('change-password/<token>/', change_password, name='change_password'),
    path('lupa-password/', lupa_password, name="lupa_password"),
    path('verif-akun/', verif_akun, name="verif_akun"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('dashboard/', DashboardPageView.as_view(), name="dashboard"),
    path('cpl-map/', CplMapPageView.as_view(), name="cpl_map"),
    path('rekap-nilai/', RekapNilaiPageView.as_view(), name="rekap_nilai"),
    path('rekap-cpl/', RekapCplPageView.as_view(), name="rekap_cpl"),
    path('nilai/', NilaiPageView.as_view(), name="nilai"),
    path('profil/', ProfilPageView.as_view(), name="profil"),
    path('user/add/', UserCreateView.as_view(), name='user_create'),
    path('user/<int:pk>/edit/', UserUpdateView.as_view(), name='user_update'),
    path('user/<int:pk>/delete/', UserDeleteView.as_view(), name='user_delete'),
    path('user/', UserListView.as_view(), name='user_list'),
    path('verifikasi-berhasil/<token>/', verif_berhasil, name='verif_berhasil'),
]