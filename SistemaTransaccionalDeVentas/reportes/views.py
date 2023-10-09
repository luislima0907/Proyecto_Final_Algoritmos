from django.shortcuts import render

# Create your views here.

def reportes_views(request):
    return render(request, 'reportes.html')