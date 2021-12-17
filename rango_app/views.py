from django.shortcuts import render
from .models import Receipts

# Create your views here.
def index(request):
    """Call the Index page for Rango Application"""
    return render(request, 'rango_app/index.html')


#TODO design view logic
def receipts(request):
    """Call the Receipt page for Rango Application"""
    receipts = Receipts.objects.all()
    context = {'receipts': receipts}
    return  render(request, 'rango_app/receipts.html', context)