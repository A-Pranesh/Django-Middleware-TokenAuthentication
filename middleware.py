import json
import re

import jwt
from django.http import HttpResponse
from Authenticate.models import Employee

class employee_middleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.method == 'POST':
            data = json.loads(request.body.decode('utf-8'))
            regex = re.compile('[a-zA-Z0-9!@#$%^&*_]+')
            if regex.search(data['name']) and regex.search(data['age']) and regex.search(data['designation']):
                pass
            else:
                return HttpResponse('Invalid data')
        else:
            try:
                token = request.META.get('HTTP_AUTHORIZATION')
                token = token.split()
                decoded = jwt.decode(token[1], "SECRET_KEY")
                name = decoded['name']
                if Employee.objects.get(name=name).id:
                    pass
                else:
                    return HttpResponse("Record not found")
            except:
                return HttpResponse("Record not found")
