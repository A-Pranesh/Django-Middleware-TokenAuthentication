import json

import jwt
from django.http import HttpResponse
from django.shortcuts import render
from .models import Employee

def post(request):
    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))
        obj = Employee()
        obj.name = data['name']
        obj.age = data['age']
        obj.designation = data['designation']
        obj.save()
        jwt_token = {'token': jwt.encode(data, "SECRET_KEY")}
        token = jwt_token['token']
        print(token)
        print(type(token))
        decoded = jwt.decode(token, "SECRET_KEY")
        print(decoded)
        return HttpResponse('SUCCESS')

def get(request):
    if request.method == "GET":
        token = request.META.get('HTTP_AUTHORIZATION')
        token = token.split()
        decoded = jwt.decode(token[1], "SECRET_KEY")
        name = decoded['name']
        return HttpResponse(Employee.objects.get(name=name))
