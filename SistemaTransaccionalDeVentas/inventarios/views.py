from django.shortcuts import render

# Create your views here.

def inventarios_views(request):
    return render(request, 'inventarios.html')