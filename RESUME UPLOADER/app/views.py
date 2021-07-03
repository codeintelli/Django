from django.shortcuts import render,redirect
from .forms import ResumeForm
from .models import Resume
from django.views import View
# Create your views here.

class HomeView(View):
    def get(self,request):
        form = ResumeForm()
        candidates = Resume.objects.all()
        return render(request, 'home.html',{'candidates':candidates,'form':form})
    def post(self, request):
        form = ResumeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return render(request,'home.html',{'form':form})
        # return redirect('/',{'form':form})

class candidateView(View):
    def get(self,request,id):
        customcandidate = Resume.objects.get(id=id)
        return render(request, 'candidate.html',{'customcandidate':customcandidate})
