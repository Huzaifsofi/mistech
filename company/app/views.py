from .models import Info
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return render(request, 'index.html')


def contact(request):

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        ph_no = request.POST['ph_no']
        subject =  request.POST['subject']
        message = request.POST['message']
        new = Info(name=name, email=email, ph_no=ph_no, subject=subject, message=message)
        new.save()
        return redirect('home')
    return render(request, 'contact.html')

def services(request):
    return render(request, 'services.html')    