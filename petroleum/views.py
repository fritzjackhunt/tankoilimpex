from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'oasis/index.html')

def about(request):
    return render(request, 'oasis/about.html')