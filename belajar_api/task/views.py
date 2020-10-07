from django.http import HttpResponse, JsonResponse
import json
from django.forms.models import model_to_dict
from .models import BelajarAPI

# Create your views here.

def belajar_api(req):
	data = BelajarAPI.objects.all()
	simpan = []

	for d in data:
		simpan.append(model_to_dict(d))
		
	return JsonResponse({
		'data': simpan
		}, safe=False)

def create(req):
	if req.method == 'POST':
		data_byte = req.body
		data_string = str(data_byte, 'utf-8')
		data = json.loads(data_string)
		
		a = BelajarAPI.objects.create(
			nama=data['nama'],
			motto=data['motto']
			)

		return JsonResponse({
			'data': model_to_dict(a),
			})

def delete(req, id):
	if req.method == 'DELETE':
		a = BelajarAPI.objects.filter(pk=id).delete()

		return JsonResponse({
			'msg':'data has been deleted'
			})

def read(req, id):
	if req.method == 'GET':
		a = BelajarAPI.objects.filter(pk=id).first()

		return JsonResponse({
			'data': model_to_dict(a),
			})

def update(req, id):
	if req.method == 'PUT':
		data_byte = req.body
		data_string = str(data_byte, 'utf-8')
		data = json.loads(data_string)
		
		a = BelajarAPI.objects.filter(pk=id).update(
			nama=data['nama'],
			motto=data['motto']
			)

		b = BelajarAPI.objects.filter(pk=id).first()

		return JsonResponse({
			'data': model_to_dict(b),
			})