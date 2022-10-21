from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'login.html')
def registration(request):
    return render(request, 'registration.html')
def forgotpassword(request):
    return render(request, 'forgotpassword.html')
def aboutus(request):
    return render(request, 'aboutus.html')
def contactus(request):
    return render(request, 'contactus.html')
def index(request):
    return render(request, 'index.html')