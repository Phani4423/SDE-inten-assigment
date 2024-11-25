from django.shortcuts import render
from app.models import *
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def tables(request):
    Webpage.objects.all()
    LPGS = Webpage.objects.all()
    d = {'LPGS': LPGS}
    return render(request,'tables.html',d)
def tables_update(request):
    
    Webpage.objects.filter(name = 'bolt').update(email = 'fastrunner@gmail.com')
    LPGS = Webpage.objects.all().order_by('name')
    d = {'LPGS': LPGS}
    return render(request,'tables_uptate.html',d)
def tables_delete(request):
    Webpage.objects.filter(name = 'phani').delete()
    LPGS = Webpage.objects.all()
    d = {'LPGS': LPGS}
    return render(request,'tables_delete.html',d)
def insert(request):
    MF = insertForm()
    d = {'MF': MF}
    if request.method == 'POST':
        MF = insertForm(request.POST)
        if MF.is_valid():
            MF.save()
            return HttpResponse('done')
        else:
            return HttpResponse('not inserted check you entered valid data')
    return render(request,'insert.html',d)
    
