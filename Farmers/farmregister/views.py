from django.shortcuts import render
from django.http import HttpResponse
from Home.models import Register

def funroute3(request):
    if request.method=="POST":
        print(request)
        print("hai")
        name=request.POST.get(name,'')
        Register=Register(name=name)
        Register.save()
    print("hai")
    return render(request,'farmregister/farmregister1.html')
    
