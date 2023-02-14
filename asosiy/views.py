from django.shortcuts import render,redirect,HttpResponse
from .models import *
def Home(request):
    data={
        'data':Todo.objects.all()
    }
    return render(request,'todo.html',data)
def HomeEdit(request,son):
    Todo.objects.get(id=son).delete()
    return redirect('/')

def qushish(request):
    if request.method=='POST':
        Todo.objects.create(
            nom=request.POST.get('nom'),
            bajarilish_vaqti=request.POST.get('vaqt'),
            batafsil=request.POST.get('batafsil'),
            status=request.POST.get('status')
            )
    return redirect('/')

def TodoEdit(request,son):
    if request.method=='POST':
        Todo.objects.filter(id=son).update(
            nom=request.POST.get('nom'),
            bajarilish_vaqti=request.POST.get('vaqt'),
            batafsil=request.POST.get('batafsil'),
            status=request.POST.get('status')
        )
        return redirect('/')
    data={
        'data':Todo.objects.get(id=son)
    }
    return render(request,'edit.html',data)