from django.shortcuts import render

# Create your views here.
def index(request):
    """Call the Index page for Rango Application"""
    return render(request, 'rango_app/index.html')