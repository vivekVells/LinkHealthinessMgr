from django.shortcuts import render
from django.http import HttpResponse

import time, requests

def index(request):
    # return HttpResponse("Hai there! Welcome to Link Healthiness Verifier")
    return render(request, 'fileuploadviewapp/index.html', {})

def verifyByFile(request):
    if request.method == 'POST':
        noerror = []
        error404 = []

        file=request.FILES['file'].read().splitlines()

        for f in file:
            decoded = f.decode("ascii")

            try:
                r = requests.get((decoded), timeout=5)

                if(int(r.status_code) == 404):
                    error404.append(decoded)
                else:
                    noerror.append(decoded)
            except requests.exceptions.ConnectionError:
                print("connection error...")

        context = {'error404' : error404, 'noerror' : noerror }
        return render(request, 'fileuploadviewapp/verifybyfile.html', context)
    else:
        return HttpResponse("File Upload Error...")

def verifyByUrl(request):
    if request.method == 'POST':
        context = {}
        return render(request, 'fileuploadviewapp/verifybyurl.html', context)
    else:
        context = {}
        return render(request, 'fileuploadviewapp/verifybyurl.html', context)