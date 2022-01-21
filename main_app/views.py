from django.shortcuts import render, redirect
from .forms import AddWidgetForm
from .models import *

# Define the home view
def index(request):
    form = AddWidgetForm()
    widgets = Widget.objects.all()
    return render(request, 'index.html', {'form': form, 'widgets': widgets})

def add_widget(request):
    form = AddWidgetForm(request.POST)

    if form.is_valid():
        new_widget = form.save(commit=False)
        new_widget.widget_id 

    return redirect('index')