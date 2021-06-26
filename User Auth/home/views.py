from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as django_logout
# Create your views here.

# password for shiva SHIV@$123
def index(request):
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request,'index.html')

def loginUser(request):
    if request.method == "POST":
        # check if user is enter correct credentials
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            login(request,user)
            return redirect('/')
        else:
            return render(request,'login.html')
            # No backend authenticated the credentials
 
    return render(request,'login.html')


def logoutUser(request):
    django_logout(request)
    return redirect('/login')