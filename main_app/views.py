from django.shortcuts import render


# Define the home view
def index(request):
  return render(request, 'index.html')