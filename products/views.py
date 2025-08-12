from django.shortcuts import render

def products_index(request):
    return render(request, 'recipes/index.html')