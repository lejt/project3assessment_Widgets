from django.forms import ModelForm
from .models import *
from django import forms

class AddWidgetForm(ModelForm):
    class Meta:
        model = Widget
        fields = '__all__'
