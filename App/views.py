from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'payements/index.html')
    return render(request,'payements/thank_you.html')