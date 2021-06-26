from django.shortcuts import render,HttpResponse
from datetime import datetime
from Home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')


# def about(request):
#     context={
#         'variable':'this is send '
#     }
#     return render(request,'about.html',context)


def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')


def contact(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('message')
        contact = Contact(name=name, email=email, phone=phone, desc=desc,date = datetime.today())
        contact.save()
        messages.success(request, 'Your Message Has Been Send Successfully!')
    return render(request,'contact.html')