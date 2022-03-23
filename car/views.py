from django.shortcuts import render

# Create your views here.

def carIndex(request):
    return render(request, 'backend/carIndex.html')