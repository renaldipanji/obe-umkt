from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout, update_session_auth_hash
from django.contrib.auth.models import Group
from .forms import *
from .models import *
from .helpers import *
import uuid
from django.views.generic import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

class DashboardPageView(LoginRequiredMixin,TemplateView):
    template_name = 'main/dashboard.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Dashboard | OBE UMKT'
        context['nama'] = self.request.user.nama
        return context

class CplMapPageView(LoginRequiredMixin,TemplateView):
    template_name = 'main/cpl_map.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'CPL map | OBE UMKT'
        context['nama'] = self.request.user.nama
        return context

class RekapNilaiPageView(LoginRequiredMixin,TemplateView):
    template_name = 'main/rekap_nilai.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Rekap nilai | OBE UMKT'
        context['nama'] = self.request.user.nama
        return context

class RekapCplPageView(LoginRequiredMixin,TemplateView):
    template_name = 'main/rekap_cpl.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Rekap CPL | OBE UMKT'
        return context

class NilaiPageView(LoginRequiredMixin,TemplateView):
    template_name = 'main/nilai.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Nilai | OBE UMKT'
        return context

class ProfilPageView(LoginRequiredMixin,UpdateView):
    template_name = 'akun/edit_profil.html'
    success_url = reverse_lazy('akun:profil')
    model = User
    success_message = "Profile updated successfully"
    form_class = ProfileForm
    second_form_class = ProfilePictureForm    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit Profil | OBE UMKT'
        if self.request.POST:
            context['picture_form'] = self.second_form_class(self.request.POST, self.request.FILES, instance=self.request.user)
        else:
            context['picture_form'] = self.second_form_class()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        picture_form = context['picture_form']
        if picture_form.is_valid():
            picture_form.save()
            messages.success(self.request, 'Foto profil berhasil diperbarui.')
        return super().form_valid(form)

    def get_object(self, queryset=None):
        return self.request.user

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        context = self.get_context_data()
        picture_form = context['picture_form']
        if 'profile' in request.POST:
            return super().post(request, *args, **kwargs)
        elif 'picture' in request.POST:
            if picture_form.is_valid():
                return self.form_valid(form)
        else:
            return self.form_invalid(form)

    # def form_valid(self, form):
    #     response = super().form_valid(form)
    #     messages.success(self.request, self.success_message)
    #     return response

    # def get_object(self, queryset=None):
    #     return self.request.user
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['title'] = 'Edit Profil | OBE UMKT'
    #     context['foto'] = self.request.user.foto_profile.path
    #     return context

class LogoutView(View):
    def post(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, 'Anda Berhasil Logout')
        return redirect('akun:login')

# Create your views here.
def daftar(request):
    form = RegisterForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            token = str(uuid.uuid4())
            profile_obj = Profile.objects.create(user = user , forgot_password_token = token)
            profile_obj.save()
            domain = request.get_host()
            ssl = request.is_secure()
            send_verif_mail(user.email, token, domain, ssl)            
            messages.success(request, 'Daftar Berhasil! Silahkan Cek Email anda untuk mengaktifkan akun')
            return redirect('akun:login')
        else:
            messages.error(request, form.errors)
            return redirect('akun:daftar')
    context={
        'form': form,
        'title':'Registrasi | OBE UMKT',
    }            
    return render(request, 'akun/registrasi.html', context)

def verif_berhasil(request, token):
    profile_obj = Profile.objects.get(forgot_password_token = token)
    user_obj = User.objects.get(id = profile_obj.user_id)
    if user_obj.is_active == False :
        user_obj.is_active = True
        user_obj.save()
        messages.success(request, 'Akun telah diverifikasi, silahkan login.')
        return redirect('akun:login')
    messages.success(request, 'Akun telah diverifikasi, silahkan login.')
    return render(request, 'akun/login.html')

def login(request):
    form = LoginForm(request.POST or None)
    if request.user.is_authenticated:
        return redirect('akun:dashboard')
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username,password=password)
            if user is not None:
                try:
                    user_group = Group.objects.get(user = user)
                except Group.DoesNotExist:
                    user_group  = None
                auth_login(request, user)
                if user_group is not None:
                    pass
                else:
                    my_group = Group.objects.get(name='pengguna')   
                    my_group.user_set.add(user)     
                redirect_url = request.GET.get('next', '/dashboard/')
                return redirect(redirect_url)
            else:
                user_id = User.objects.filter(username=username).first()
                messages.error(request, 'Username atau Password tidak valid')
                return redirect('akun:login')
                if user_id:
                    if not user_id.is_active:
                        messages.error(request, 'User Belum Aktif Silahkan Verifikasi Email Dulu')
                        return redirect('akun:login')
                else:
                    messages.error(request, 'Username atau Password tidak valid')
                    return redirect('akun:login')
        else:
            messages.error(request, 'Validasi form error')
        print(form.errors)
    context = {
        'form':form,
        'title':'Login | OBE UMKT'
    }
    return render(request, 'akun/login.html', context)


def verif_akun(request):
    form = EmailForm(request.POST or None)
    try:
        if request.method == 'POST' and form.is_valid():
            email = form.cleaned_data.get('email')
            if not User.objects.filter(email = email).first():
                messages.error(request, 'Email tidak ditemukan.')
                return redirect('verifikasi_akun')
            user_obj = User.objects.get(email = email)
            token = str(uuid.uuid4())
            profile_obj = Profile.objects.get(user_id = user_obj.id)
            profile_obj.forgot_password_token = token
            profile_obj.save()
            domain = request.get_host()
            ssl = request.is_secure()
            send_verif_mail(user_obj.email, token, domain, ssl)
            messages.success(request, 'Kami telah mengirimkan verifikasi akun anda di email!')            
            return redirect('akun:login')
    
    except Exception as e:
        print (e)         
    return render(request, 'akun/verif_akun.html', {'form':form})


def lupa_password(request):
    form = EmailForm(request.POST or None)
    try:
        if request.method == 'POST' and form.is_valid():
            email = form.cleaned_data.get('email')

            if not User.objects.filter(email = email).first():
                messages.error(request, 'Email tidak ditemukan.')
                return redirect('akun:lupa_password')
            user_obj = User.objects.get(email = email)
            token = str(uuid.uuid4())
            profile_obj = Profile.objects.get(user_id = user_obj.id)
            profile_obj.forgot_password_token = token
            profile_obj.save()
            domain = request.get_host()
            ssl = request.is_secure()
            send_forget_password_mail(user_obj.email, token, domain, ssl)
            messages.success(request, 'Cek email anda untuk mendapatkan akses reset password')
            return redirect('akun:lupa_password')
    
    except Exception as e:
        print (e)    
    context = {
        'form': form,
        'title': "Kirim Reset Password | OBE UMKT",
    }
    return render(request, 'akun/email_reset_password.html', context)

def change_password(request, token):
    try:
        form = ChangePasswordForm(request.POST or None)
        context = {
            'form':form,
            'title': 'Reset Password | OBE UMKT',
            }
        if request.method == 'POST' and form.is_valid():
            new_password = form.cleaned_data.get('new_password')
            confirm_password = form.cleaned_data.get('reconfirm_password')
            profile_obj = Profile.objects.get(forgot_password_token = token)
            user_id = profile_obj.user.id
            
            if user_id is  None:
                messages.success(request, 'User tidak ditemukan.')
                return redirect(f'/change-password/{token}/')        
            
            if  new_password != confirm_password:
                messages.success(request, 'Password tidak sama.')
                return redirect(f'/change-password/{token}/')
            user_obj = User.objects.get(id = user_id)
            user_obj.set_password(new_password)
            user_obj.save()
            messages.success(request, 'Password berhasil diganti.')
            return redirect('akun:login')
    except Exception as e:
        print(e)
    return render(request, 'akun/change_password.html', context)

class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'user/user_list.html'
    context_object_name = 'users'
    ordering = ['username']
    paginate_by = 10

class UserCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = User
    template_name = 'user/user_create.html'
    fields = ['username', 'first_name', 'last_name', 'email', 'password']
    success_url = reverse_lazy('akun:user_list')
    success_message = "User created successfully"

    def form_valid(self, form):
        form.instance.set_password(form.cleaned_data['password'])
        response = super().form_valid(form)
        return response

class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    template_name = 'user/user_update.html'
    fields = ['username', 'first_name', 'last_name', 'email']
    success_url = reverse_lazy('akun:user_list')
    success_message = "User updated successfully"

class UserDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = User
    template_name = 'user/user_confirm_delete.html'
    success_url = reverse_lazy('akun:user_list')
    success_message = "User deleted successfully"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)
