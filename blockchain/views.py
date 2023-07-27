from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json

# Create your views here.
def db_test(request):
    if request.method == "POST":
        #print(request.POST)
        #body = json.loads(request.body)
        #name = body["name"]
        data = {
            "name": "choi",
            "age": 20,
            "hobbies": ["Coding", "Art", "Gaming", "Cricket", "Piano"]
        }
        print(data)
        return JsonResponse(data, safe = False)
    else:
        return HttpResponse("Hello API")