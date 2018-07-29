from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # return HttpResponse("Hai there! Welcome to Link Healthiness Verifier")
    return render(request, 'fileuploadviewapp/index.html', {})