from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout, update_session_auth_hash
from django.contrib.auth.models import Group
from .models import *
import uuid
from django.views.generic import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin


# Create your views here.
class MatkulPageView(LoginRequiredMixin, ListView):
    template_name = 'main/daftar_mata_kuliah.html'
    model = Matkul
    context_object_name = 'matkuls'
    ordering = ['nama']
    paginate_by = '10'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Daftar mata kuliah | OBE UMKT'
        context['nama'] = self.request.user.nama
        return context

class MatkulPengukurPageView(LoginRequiredMixin, ListView):
    template_name = 'main/daftar_mata_kuliah_pengukur.html'
    model = Matkul
    context_object_name = 'matkuls'
    ordering = ['nama']
    paginate_by = '10'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Daftar mata kuliah | OBE UMKT'
        context['nama'] = self.request.user.nama
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(matkul_pengukur='Ya')
        return queryset

class CreateMatkulPageView(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    template_name = 'main/tambah_matkul.html'
    model = Matkul
    fields = ['pemilik', 'prodi', 'kode_matkul', 'nama', 'jumlah_sks','semester','matkul_pengukur','keterangan','rps']
    success_message = "Mata Kuliah Berhasil Ditambahkan"
    success_url = reverse_lazy('obe:matkul')

    def form_valid(self, form):
        response = super().form_valid(form)
        return response    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Daftar mata kuliah | OBE UMKT'
        context['judul'] = 'Tambah mata kuliah'
        context['nama'] = self.request.user.nama
        return context

class UpdateMatkulPageView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'main/tambah_matkul.html'
    model = Matkul
    fields = ['pemilik', 'prodi', 'kode_matkul', 'nama', 'jumlah_sks','semester','matkul_pengukur','keterangan','rps']
    success_message = "Mata Kuliah Berhasil Di Update"
    success_url = reverse_lazy('obe:matkul')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['title'] = 'Edit mata kuliah | OBE UMKT'
    #     context['judul'] = 'Edit mata kuliah'

class DetailMatkulPengukurPageView(LoginRequiredMixin,DetailView):
    template_name = 'main/lihat_matkul_pengukur.html'
    model = Matkul
    context_object_name = 'matkul'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Detail Mata Kuliah Pengukur | OBE UMKT'
        return context