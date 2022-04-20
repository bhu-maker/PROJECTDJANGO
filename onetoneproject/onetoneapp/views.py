from unicodedata import name
from django.shortcuts import redirect, render
from .import models
from .import forms
# Create your views here.


def placenew(request):
    obj=forms.placeform()
    if request.method== "POST":
        obj=forms.placeform(request.POST)
        if obj.is_valid():
            obj.save()
            return redirect("home/list")
    return render(request,"placenew.html",{"sub":obj})        

def restnew(request):
    obj=forms.restaurantform()
    if request.method== "POST":
        obj=forms.restaurantform(request.POST)
        if obj.is_valid():
            obj.save()
            return redirect("home/list")
    return render(request,"restaurantnew.html",{"rest":obj})        


def waitnew(request):
    obj=forms.waiterform()
    if request.method== "POST":
        obj=forms.waiterform(request.POST)
        if obj.is_valid():
            obj.save()
            return redirect("home/list")
    return render(request,"waiternew.html",{"sub":obj})    


def display(request):
    res=models.Restaurant.objects.all()
    wai=models.Waiter.objects.all()
    n1=models.Waiter.objects.get(name='joe').restaurant_id
    print(n1)
    r1=models.Place.objects.get(id=n1)
    print(r1)
    n2=models.Waiter.objects.filter(restaurant_id=3)
    print(n2)
    print(len(n2))
   

    return render (request,"disp.html",{"key":res,"key1":wai,"key2":n2})


def projectdisplay(request):
    p=models.Person.objects.all()
    return render(request,"projectdisp.html",{"key":p})

def irctc(request,pk):
      p=models.Person.objects.filter(project_id=pk) 
      return render(request,"irctc.html",{"key":p})

def irctcname(request):
      p=models.Person.objects.get(project_name="irctc") 
      return render(request,"irctc.html",{"key":p})

def projectall(request):
      p=models.Project.objects.all() 
      return render(request,"irctc.html",{"key":p})













def listing(request):
    obj=models.Place.objects.get(restaurant__place__name__startswith="JOJO")
    print(obj)

    print(type(obj))

    return render(request,"list.html",{"key":obj})

def listingall(request):
    obj=models.Place.objects.all()
    obj1=models.Restaurant.objects.all()
    obj2=models.Waiter.objects.all()
    print(obj,obj1,obj2)

    print(type(obj))

    return render(request,"list.html",{"key":obj,"key1":obj1,"key2":obj2})    