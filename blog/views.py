from django.shortcuts import render

# Create your views here.
def hello_page(request):
    return render(request, 'index.html')