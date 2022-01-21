from hashlib import new
from django.shortcuts import render, redirect
from .forms import AddWidgetForm
from .models import *
from django.db.models import Sum

# Define the home view
def index(request):
    form = AddWidgetForm()
    widgets = Widget.objects.all()
    sum = widgets.aggregate(Sum('quantity'))
    return render(request, 'index.html', {'form': form, 'widgets': widgets, 'sum': sum})

def add_widget(request):
    form = AddWidgetForm(request.POST)
    if form.is_valid():
        new_widget = form.save()    
        
    return redirect('index')

def delete_widget(request, widget_id):
    widget = Widget.objects.get(id=widget_id)
    widget.delete()
    return redirect('index')
