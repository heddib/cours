from django.shortcuts import render, redirect, get_object_or_404

from module_cours.models import Cours
from module_cours.forms import CoursForm
from django.http import HttpResponseRedirect

def index(request):
    cours = Cours.objects.all()
    context = { 'cours': cours }
    return render(request, 'cours/index.html', context)

def create(request):
    if request.method == 'POST':
        form = CoursForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/cours/')
    else:
        form = CoursForm()

    return render(request, 'cours/create/index.html', {'form': form})

def show(request, id):
    cours = get_object_or_404(Cours, id=id)
    return render(request, 'cours/show/index.html', {'cours': cours})

def update(request, id):
    cours = get_object_or_404(Cours, id=id)
    if request.method == 'POST':
        form = CoursForm(request.POST, instance=cours)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/cours/')
    else:
        form = CoursForm(instance=cours)
    return render(request,'cours/update/index.html', {'form': form})

def delete(request, id):  
    cours = get_object_or_404(Cours, id=id)  
    cours.delete()  
    return redirect("/cours/")