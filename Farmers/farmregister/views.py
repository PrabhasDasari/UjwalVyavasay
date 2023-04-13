from django.shortcuts import render
from Home.models import Register

def funroute3(request):
    if request.method=="POST":
        name=request.POST.get('name','')
        reg =Register(name=name)
        reg.save()
    return render(request,'farmregister/farmregister1.html')
    
