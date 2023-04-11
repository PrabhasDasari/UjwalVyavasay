from django.shortcuts import render
from django.http import HttpResponse
from Home.models import Register

def funroute3(request):
    if request.method=="POST" :
        print(request)
        name=request.POST.get(name,'')
        Register=Register(name=name)
        Register.save()
    return render(request,'farmregister/farmregister1.html')
