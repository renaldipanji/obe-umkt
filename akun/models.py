from django.db import models
from django.db.models.deletion import CASCADE
import datetime
import os
import uuid


from django.contrib.auth.models import AbstractUser

def imagepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/profil/', filename)

class ProdiModel(models.Model):
    nama_prodi = models.TextField(blank=True)
    
    def __str__(self):
        return self.nama_prodi
class User(AbstractUser):
    nama = models.CharField(max_length=30, blank=True, verbose_name='Nama')
    foto_profile = models.ImageField(upload_to = imagepath, null=True, blank=True)
    prodi = models.ForeignKey(ProdiModel, on_delete=models.CASCADE,null=True)

    def save(self, *args, **kwargs):
        # Panggil method save dari parent class
        super(User, self).save(*args, **kwargs)

        # Cek apakah instance Profile sudah ada
        try:
            self.profile
        except Profile.DoesNotExist:
            # Jika belum, buat instance Profile baru
            Profile.objects.create(
                user=self,
                forgot_password_token=str(uuid.uuid4())
            )
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    forgot_password_token = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add = True )
