from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest

from .models import Task
from .forms import TaskForm

def index(request: HttpRequest):
    tasks = Task.objects.order_by('-id')

    num_visit = request.session.get('num_visit', 0) # это куки
    request.session['num_visit'] = num_visit + 1 #

    context = {
        'title': 'Главная страница сайта',
        'tasks': tasks,
        'num_visit': num_visit,
    }
    return render(request, 'MyApp/index.html', context)


def about(request: HttpRequest):
    return render(request, 'MyApp/about.html')


def create(request: HttpRequest):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'form iivalid and oguzok'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'MyApp/create.html', context)
