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
