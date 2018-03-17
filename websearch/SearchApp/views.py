from django.shortcuts import render


def index(request):
    return render(request, 'SearchApp/index.html')

def yourimages(request):
    return render(request, 'SearchApp/yourimages.html')