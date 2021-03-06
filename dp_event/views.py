from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render_to_response,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from dp_event.models import*
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from django.utils import timezone
from django.shortcuts import render,get_object_or_404
from django.template import RequestContext,loader
from django.core.urlresolvers import reverse
from dp_event.models import pengguna
from dp_event.models import Visitor
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from dp_event.models import Event
from dp_event.forms import formevent
from dp_event.form import form_login
from dp_event.form import form_username
from dp_event.form import form_daftar
from django.utils.timesince import timesince
from django.shortcuts import render,render_to_response,RequestContext



# Create your views here.
def index(request):

	list_event=Event.objects.filter().order_by('date_begin')[:3]
	album = galery.objects.filter()[:10]
	daftar_event=Event.objects.filter().order_by('date_begin')[3:]
	form = form_login
	daftar = form_daftar
	username = form_username
	now=timezone.now()
	#tes tes tes

	#if request.user.is_authenticated():
		#return HttpResponseRedirect('/')


	return render_to_response('list_event.html',{'list_event':list_event,'time':now,'form':form,'daftar':daftar,'username':username,'album':album,'daftar_event':daftar_event})


@login_required(login_url='/#muncul4')
def detail_event(request,id_event):

	event = Event.objects.get(id=int(id_event))
	list_event=Event.objects.filter().order_by('date_begin')[:3]
	now = datetime.now()
	list_visitor = Visitor.objects.filter(target_event = id_event,status=True)
	list_visitor_belum = Visitor.objects.filter(target_event = id_event,status=False,date_join__gte=datetime.now()-timedelta(hours=24))

	return render_to_response('detail_event.html',	{'event':event,'list_visitor':list_visitor,'id':request.user.id,'list_event':list_event,'list_visitor_belum':list_visitor_belum})



@login_required
def join_event(request,id_event,id_user):
		list_event=Event.objects.filter().order_by('date_begin')[:3]
		user = User.objects.get(id=int(id_user))
		event = Event.objects.get(id=int(id_event))

		args = {}
		args.update(csrf(request))
 		args.update({'event':event,'user':user,'id':request.user.id,'list_event':list_event})

		return render_to_response('form_event.html',args)


@login_required(login_url='/#muncul4')
def process_join_event(request, id_event):
	event=Event.objects.filter(id=int(id_event))
	list_event=Event.objects.filter().order_by('date_begin')[:3]
	event.id=id_event
	name=request.POST['name']
	user_id=request.POST['id_user']
	jenis_kelamin=request.POST['jk']
	phone = request.POST['phone']
	email = request.POST['email']
	no_ktp = request.POST['no_ktp']
	kota = request.POST['kota']
	alamat = request.POST['alamat']
	Keterangan = request.POST['keterangan']
	target_event = event


	form = formevent()
	return render_to_response('form_event2.html',{'form':form,'event':event,'name':name,'jenis_kelamin':jenis_kelamin,'phone':phone,'email':email,'no_ktp':no_ktp,'kota':kota,'alamat':alamat,'id_event':id_event,'user_id':user_id,'Keterangan':Keterangan,'list_event':list_event})
	#event = Event.objects.get(id=id_event)

	#visitor = Visitor(
		#name=request.POST['name'],
		#user_id=request.POST['id_user'],
		#jenis_kelamin=request.POST['jk'],
		#phone = request.POST['phone'],
		#email = request.POST['email'],
		#no_ktp = request.POST['no_ktp'],
		#kota = request.POST['kota'],
		#alamat = request.POST['alamat'],
		#Keterangan = request.POST['keterangan'],
		#target_event = event
	#)
	#visitor.save()
	#if id_event:
	#	count = event.tersedia
	#	count -= 1
	#	event.tersedia = count
	#	event.save()


	#	return HttpResponseRedirect('/event/' + request.POST['id_event']  )

@login_required(login_url='/#muncul4')
def process_join_event2(request, id_event):
	event = Event.objects.get(id=int(id_event))

	visitor = Visitor(
		name=request.GET['nama'],
		user_id=request.GET['user_id'],
		jenis_kelamin=request.GET['jk'],
		phone = request.GET['phone'],
		email = request.GET['email'],
		no_ktp = request.GET['no_ktp'],
		kota = request.GET['kota'],
		alamat = request.GET['alamat'],
		Keterangan = request.GET['keterangan'],
		date_join = datetime.now(),
		target_event = event,
	)
	visitor.save()
	if id_event:
		count = event.tersedia
		count -= 1
		event.tersedia = count
		event.save()
	tik = event.tiket
	nomor = tik - count
	Peserta = peserta(
		user_id = request.GET['user_id'],
		nama_peserta = request.GET['peserta_satu'],
		no_tiket = nomor
	)
	Peserta.save()
	Pes = peserta(
		user_id = request.GET['user_id'],
		nama_peserta = request.GET['peserta_dua'],
		no_tiket = nomor +1
	)
	Pes.save()
	Pese = peserta(
		user_id = request.GET['user_id'],
		nama_peserta = request.GET['peserta_tiga'],
		no_tiket = nomor +2
	)
	Pese.save()
	Peser = peserta(
		user_id = request.GET['user_id'],
		nama_peserta = request.GET['peserta_empat'],
		no_tiket = nomor +3
	)
	Peser.save()
	Pesert= peserta(
		user_id = request.GET['user_id'],
		nama_peserta = request.GET['peserta_lima'],
		no_tiket = nomor +4
	)
	Pesert.save()
	return HttpResponseRedirect('/event/' + id_event  )

def daftar(request):
	return render_to_response('daftar.html')

def proses_daftar(request):
#masih error apabila memakai method post ,forbiden csrf
	list_event=Event.objects.filter().order_by('date_begin')[:3]

	form = form_daftar(request.GET,  request.FILES)
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')
	if request.method == 'GET':
		form = form_daftar(request.GET,  request.FILES)

		u = User(username=request.GET['username'] , password=request.GET['password'])
		u.save()
		u.set_password(u.password)
        	u.save()
		form = form_daftar(request.GET, request.FILES)
		Pengguna = pengguna(
			user = u,
			nama_depan = request.GET['first_name'],
			nama_belakang = request.GET['last_name'],
			jenis_kelamin = request.GET['jk'],
			email = request.GET['email'],
			no_ktp = request.GET['no_ktp'],
			kota = request.GET['kota'],
			alamat = request.GET['alamat'],
			telepon = request.GET['telepon'],
			telepon2 = request.GET['telepon'],
			foto = request.GET['foto'],
		)
		Pengguna.save()
		subject = 'Konfirmasi Akun'
		message = 'Selamat datang.\n  \n Silahkan konfirmasi akun anda dengan meng-klik link dibawah ini jika memang email yang anda konfirmasikan benar./n'+'127.0.0.1:8000/accounts/loggedin/konfirmasi/email/'+str(request.user.id)
		from_email = settings.EMAIL_HOST_USER
		to_list = [Pengguna.email,settings.EMAIL_HOST_USER]
		send_mail(subject,message,from_email,to_list,fail_silently=True)
		forms = form_login
		daftar = form_daftar
		return HttpResponseRedirect('/',{'list_event':list_event,'form':forms,'daftar':daftar})
	else:


		return render_to_response('list_event.html',{'list_event':list_event})


def proses_daftar_pengguna(request,id_user):
	guna = pengguna.objects.get(user_id=int(id_user))
	user = pengguna.objects.filter(user_id=id_user)
	us = User.objects.get(id=id_user)
	image = get_object_or_404(pengguna, user_id=id_user)
	if id_user:
		us.username = request.GET['username']
		us.save()
		guna.nama_depan = request.GET['nama_depan']
		guna.nama_belakang = request.GET['nama_belakang']
		guna.jenis_kelamin = request.GET['jk']
		guna.email = request.GET['email']
		guna.no_ktp = request.GET['no_ktp']
		guna.kota = request.GET['kota']
		guna.alamat = request.GET['alamat']
		guna.telepon = request.GET['telepon']
		guna.telepon2 = request.GET['telepon']

		guna.save()
		return render_to_response('profile.html',{'profile':profile,'id':request.user.id,'pengguna':pengguna,'image':image})

def login(request):

	c = {}
	c.update(csrf(request))

	return render_to_response('list_event.html')

def kudu_login(request):
	list_event=Event.objects.filter().order_by('date_begin')[:3]
	album = galery.objects.filter()[:10]
	daftar_event=Event.objects.filter().order_by('date_begin')[3:]
	form = form_login
	daftar = form_daftar
	username = form_username
	return render_to_response('list_event.html',{'list_event':list_event,'form':form,'daftar':daftar,'username':username,'album':album,'daftar_event':daftar_event})


def auth_view(request):

	if request.user.is_authenticated():

		return HttpResponseRedirect('/')#/accounts/loggedin/#muncul
	if request.method == 'GET':
		username = request.GET.get('username', '')
		password = request.GET.get('password', '')
		user = auth.authenticate(username=username, password=password)

		if user is not None:
			auth.login(request, user)
			return HttpResponseRedirect('/accounts/loggedin/#muncul')
		else:
			return HttpResponseRedirect('/accounts/invalid/#muncul3')


def loggedin(request):
	list_event=Event.objects.filter().order_by('date_begin')[:3]
	album = galery.objects.filter()[:10]
	daftar_event=Event.objects.filter().order_by('date_begin')[3:]
	form = form_login
	daftar = form_daftar
	username = form_username
	log = pengguna.objects.get(user_id=request.user.id)
	if request.user.is_authenticated():

		if log.aktifasi == False:


			return HttpResponseRedirect('/accounts/invalid/#muncul5',{'list_event':list_event,'id':request.user.id,'form':form,'daftar':daftar,'username':username,'album':album})
		else:
			return render_to_response('loggedin.html',{'full_name':request.user.username,'list_event':list_event,'id':request.user.id,'form':form,'daftar':daftar,'username':username,'album':album,'daftar_event':daftar_event})



def invalid_login(request):
	list_event=Event.objects.filter().order_by('date_begin')[:3]
	album = galery.objects.filter()[:10]
	daftar_event=Event.objects.filter().order_by('date_begin')[3:]
	form = form_login
	daftar = form_daftar
	username = form_username
	return render_to_response('list_event.html',{'list_event':list_event,'form':form,'daftar':daftar,'username':username,'id':request.user.id,'album':album,'daftar_event':daftar_event})

def logout(request):
	list_event=Event.objects.filter().order_by('date_begin')[:3]
	album = galery.objects.filter()[:10]
	daftar_event=Event.objects.filter().order_by('date_begin')[3:]
	form = form_login
	daftar = form_daftar
	username = form_username

	auth.logout(request)
	return render_to_response('list_event.html',{'list_event':list_event,'form':form,'daftar':daftar,'username':username,'album':album,'daftar_event':daftar_event})



def profile(request,id_user):
	profile = User.objects.filter(id=id_user)
	user = pengguna.objects.filter(user_id=id_user)
	image = get_object_or_404(pengguna, user_id=id_user)
	return render_to_response('profile.html',{'profile':profile,'id':request.user.id,'pengguna':pengguna,'image':image})

def register_user(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/accounts/register_success')

	args = {}
	args.update(csrf(request))

	args['form'] = UserCreationForm()

	return render_to_response('register.html', args)



def register_success(request):
	return render_to_response('register_success.html')

def data_profile(request,id_user):
	now = datetime.now()-timedelta(hours=24)
	riwayat = Visitor.objects.filter(user_id=id_user,date_join__gte=datetime.now()-timedelta(hours=24))
	confirm = Visitor.objects.filter(user_id=id_user,date_join__lte=datetime.now()-timedelta(hours=24))
	tiket = Visitor.objects.filter(user_id=id_user,date_join__lte=datetime.now()-timedelta(hours=24))

	for join in tiket:

		event = Event.objects.get(id=int(join.target_event_id))
   		tersedia = event.tersedia
		tersedia += 1
		event.tersedia  = tersedia
    		event.save()
		pass

	return render_to_response('data_profile.html',{'riwayat':riwayat,'id':request.user.id,'now':now,'confirm':confirm})

def change_password(request,id_user):
	riwayat = Visitor.objects.filter(user_id=id_user)
	return render_to_response('change_password.html',{'riwayat':riwayat,'id':request.user.id})

def proses_change_password(request,id_user):
	passw = request.GET['password_baru']
	confirm=request.GET['confirm_password']


	if passw==confirm:
		u=User.objects.get(id=id_user)
		u.set_password(passw)
		u.save
		return render_to_response('profile.html')
	else:
		return render_to_response('loggedin.html')


@login_required(login_url='/#muncul4')
def konfirmasi(request,id_event,id_user,id_visitor):
	event = Event.objects.filter(id=int(id_event))
	visitor = Visitor.objects.filter(target_event = id_event,id=id_visitor)
	return render_to_response('konfirmasi.html',{'event':event,'visitor':visitor,'id':request.user.id})

def proses_konfirmasi(request,id_visitor):
	riwayat = Visitor.objects.filter(user_id=request.user.id,date_join__gte=datetime.now()-timedelta(hours=24))
	confirm = Visitor.objects.filter(user_id=request.user.id,date_join__lte=datetime.now()-timedelta(hours=24))
	visit = Visitor.objects.get(id=int(id_visitor))

	if id_visitor:
		nama_rekening = visit.nama_rekening
		nama_rekening = request.GET['nama_rekening']
		visit.nama_rekening = nama_rekening
		bank = visit.bank
		bank = request.GET['bank']
		visit.bank = bank
		bukti = visit.bukti
		bukti = request.GET['bukti']
		visit.bukti = bukti
		visit.save()
	proses = 'proses '
	return render_to_response('data_profile.html',{'riwayat':riwayat,'id':request.user.id,'proses':proses,'confirm':confirm})

@login_required(login_url='/#muncul4')
def cetak_tiket(request):
	riwayat = Visitor.objects.filter(user_id=request.user.id,date_join__gte=datetime.now()-timedelta(hours=24))
	confirm = Visitor.objects.filter(user_id=request.user.id,date_join__lte=datetime.now()-timedelta(hours=24))
	return render_to_response('print_login.html',{'riwayat':riwayat,'id':request.user.id,'confirm':confirm})

def konfirmasi_email(request,id_user):
	a = pengguna.objects.get(user_id=int(id_user))
	list_event=Event.objects.filter().order_by('date_begin')[:3]
	album = galery.objects.filter()[:10]
	daftar_event=Event.objects.filter().order_by('date_begin')[3:]
	form = form_login
	daftar = form_daftar
	username = form_username
	if id_user:
		aktif = a.aktifasi
		aktif = True
		a.aktifasi = aktif
		a.save()
		return render_to_response('loggedin.html',{'full_name':request.user.username,'list_event':list_event,'id':request.user.id,'form':form,'daftar':daftar,'username':username,'album':album,'daftar_event':daftar_event})

def ganti_email(request,id_user):
	b = pengguna.objects.get(user_id=int(id_user))
	list_event=Event.objects.filter().order_by('date_begin')[:3]
	username = form_username
	form = form_login
	daftar = form_daftar
	if id_user:
		mail = b.email
		mail = request.GET['email']
		b.email = mail
		b.save()
		return HttpResponseRedirect('/accounts/loggedin/email')

def email(request):
	list_event=Event.objects.filter().order_by('date_begin')[:3]
	username = form_username
	form = form_login
	daftar = form_daftar
	kode = request.user.id
	e = pengguna.objects.get(user_id=request.user.id)
	subject = 'Konfirmasi Akun'
	message = 'Selamat datang./n  /n Silahkan konfirmasi akun anda dengan meng-klik link dibawah ini jika memang email yang anda konfirmasikan benar./n '+'127.0.0.1:8000/accounts/loggedin/konfirmasi/email/'+str(request.user.id)
	from_email = settings.EMAIL_HOST_USER
	to_list = [e.email,settings.EMAIL_HOST_USER]
	send_mail(subject,message,from_email,to_list,fail_silently=True)
	return render_to_response('list_event.html',{'list_event':list_event,'form':form,'daftar':daftar,'username':username})

def galeri_page(request):
	list_event=Event.objects.filter().order_by('date_begin')[:3]
	album = galery.objects.filter()[:10]
	daftar_event=Event.objects.filter().order_by('date_begin')[3:]
	form = form_login
	daftar = form_daftar
	username = form_username
	galeri = Event.objects.filter()
	now=timezone.now()

	return render_to_response('galeri_page.html',{'list_event':list_event,'time':now,'form':form,'daftar':daftar,'username':username,'album':album,'daftar_event':daftar_event,'galeri':galeri,'id':request.user.id})

def detail_galeri_page(request,id_event):
	galeri = galery.objects.filter(id=id_event)
	events = galery.objects.filter(events_id=id_event)
	album = galery.objects.filter()[:10]
	galerys = Event.objects.filter()[:3]

	return render_to_response('detail_galeri_page.html',{'album':album,'galeri':galeri,'events':events,'galerys':galerys,'id':request.user.id})


def term_condition(request):

	return render_to_response('term.html')
