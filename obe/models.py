from django.db import models
from django.db.models.deletion import CASCADE
import datetime
import os
from akun.models import *
from django.contrib.auth.models import AbstractUser


# Create your models here.
choice_pengukur = (
    ('Ya', 'Ya'),
    ('Tidak', 'Tidak'),
)

def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/rps/', filename)

class Matkul(models.Model):
    pemilik = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    prodi = models.ForeignKey(ProdiModel, on_delete=models.CASCADE,null=True)
    kode_matkul = models.CharField(max_length = 10, blank=True)
    nama = models.CharField(max_length = 50, blank=True)
    jumlah_sks = models.CharField(max_length = 1, blank=True)
    semester = models.CharField(max_length = 2, blank=True)
    matkul_pengukur = models.CharField(choices=choice_pengukur, max_length=10, blank=True)
    keterangan = models.CharField(max_length = 10, blank=True)
    rps = models.FileField(upload_to = filepath, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add = True )

    def __str__(self):
        return self.kode_matkul + ' | ' + self.nama 
    