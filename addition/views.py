import time

from django.http import HttpResponse
from django.shortcuts import render


def Index(request):
    return render(request, 'index.html')


def Addition(request):
    # Just to Check Preloader
    time.sleep(3)
    if request.method == 'POST': 
        try :  
            sum = int(request.POST['first_number']) + int(request.POST['second_number'])
            return HttpResponse(str(sum))
        except :
            return HttpResponse("Invalid Data!")
    else:
        return HttpResponse("Error!")

