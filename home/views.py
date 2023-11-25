from django.shortcuts import render ,HttpResponse

from .models import Hostel


def home(request):
   
    return render(request, 'index.html') 

def hostel(request):
    my_list1 = Hostel.objects.all()
    # make it a json data
    my_list = list(my_list1.values())
    
    return render(request, 'hostel.html', {'my_list': my_list})