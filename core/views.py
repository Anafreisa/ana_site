from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'index.html')


def cv(request):
    return render(request, 'cv.html')
