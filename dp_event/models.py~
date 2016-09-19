from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model):
	title = models.CharField(max_length=50)
	organizer = models.CharField(max_length=30)
	venue = models.TextField()
	about = models.TextField(blank=True)
	poster = models.ImageField(upload_to="poster")
	tiket = models.IntegerField()
	tersedia = models.IntegerField()
	harga = models.CharField(max_length=10)
	finished = models.BooleanField()
	cetak_tiket = models.ImageField(upload_to="tiket")
	date_begin = models.DateTimeField()
	date_end = models.DateTimeField()
	date_created = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.title
	
	class Meta:
		ordering = ['date_begin']


class Visitor(models.Model):
	user = models.ForeignKey(User)
	name = models.CharField(max_length=50)
	jenis_kelamin = models.CharField(max_length=15)
	phone = models.CharField(max_length=15)
	email = models.EmailField()
	no_ktp = models.CharField(max_length = 25)
	kota = models.CharField(max_length=35)
	alamat = models.CharField(max_length = 55)
	Keterangan = models.CharField(max_length=35)
	peserta = models.CharField(max_length=55)
	date_join = models.DateTimeField()
	target_event = models.ForeignKey(Event)
	nama_rekening = models.CharField(max_length=35)
	bank = models.CharField(max_length=25)
	bukti	= models.ImageField(upload_to="konfirmasi")
	status = models.BooleanField(default=False)


	def __unicode__(self):
		return self.name
	def admin_image(self):
		return '<img src="%s"/>' % self.bukti
	admin_image.allow_tags = True

	class Meta:
		ordering = ['date_join']


class pengguna(models.Model):
	user = models.OneToOneField(User)
	jenis_kelamin = models.CharField(max_length=15)
	nama_depan = models.CharField(max_length = 30)
	nama_belakang = models.CharField(max_length = 30)
	email = models.EmailField()
	no_ktp = models.CharField(max_length = 25)
	kota = models.CharField(max_length=35)
	alamat = models.CharField(max_length = 55)
	telepon = models.CharField(max_length = 12)
	telepon2 = models.CharField(max_length = 12)
	foto	= models.FileField(upload_to="photo")
	aktifasi = models.BooleanField(default=False)

	def __unicode__(self):
		return self.nama_depan



class peserta(models.Model):
	user= models.ForeignKey(User)
	nama_peserta = models.CharField(max_length=35)
	no_tiket = models.IntegerField()

	def __unicode__(self):
		return self.nama_peserta

class galery(models.Model):
	events = models.ForeignKey(Event)
	album = models.ImageField(upload_to="galery")
	
		
