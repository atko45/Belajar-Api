from django.http import JsonResponse
from . import models

# Create your views here.

def belajar_api(req):
	# if req.GET:
	# 	models.BelajarAPI.objects.create(nama=req.GET['nama'], motto=req.GET['motto'],)

	data = models.BelajarAPI.objects.all()
	simpan = []

	for d in data:
		simpan.append({
			'nama': d.nama,
			'motto': d.motto,
			})
		
	return JsonResponse({
		'data': simpan
		}, safe=False)