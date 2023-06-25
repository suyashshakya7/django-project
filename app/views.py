from django.shortcuts import render, redirect
from .models import Patient
from django.contrib import messages

# Create your views here.
def index(request):
    data=Patient.objects.all()
    context={"data":data}
    return render(request,"index.html",context)

def insertData(request):

    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        age=request.POST.get('age')
        num=request.POST.get('num')
        gender=request.POST.get('gender')
        query=Patient(name=name,email=email,age=age,gender=gender,num=num) 
        query.save()
        messages.info(request,"Data Inserted Succesfully")
        return redirect("/")

    return render(request,"index.html")

def updateData(request,id):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        age=request.POST.get('age')
        num=request.POST.get('num')
        gender=request.POST.get('gender')
        edit=Patient.objects.get(id=id)
        edit.name=name
        edit.email=email
        edit.gender=gender
        edit.age=age
        edit.num=num
        edit.save()
        messages.warning(request,"Data Updated Succesfully")
        return redirect("/")

    d=Patient.objects.get(id=id)
    context={"d":d}
    return render(request,"edit.html",context)

def deleteData(request,id):
    d=Patient.objects.get(id=id)
    d.delete()
    messages.error(request,"Data Deleted Succesfully")
    return redirect("/")

def about(request):
    return render(request,"about.html")