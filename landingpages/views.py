from django.shortcuts import render

# Create your views here.
def landingpages(request):
    return render(request, 'landingpages/landingpages.html')