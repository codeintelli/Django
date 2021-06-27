from django.http import HttpResponse
from django.shortcuts import render
# testing
# def index(request):
#     return HttpResponse('''hello shiva mahadev \n <a href="https://google.com">Google</a>''')

# def usingHtml(request):
#     return HttpResponse("<h1>hello shiva mahadev</h1>")

# def index(request):
#     params={'name':'shiva','place':'kailash'}
#     return render(request,'index.html',params)
    
def index(request):
    return render(request,'index.html')

def analyze(request):
    # get the text from index.html file
    getText = request.GET.get('mainText','default')
    removepunc = request.Get.get('removepunc','default')
    # print(CheckremovePunc)
    # print(getText)
    analyzed = getText
    params = {'prupose':'Remove Punchuation','analyzed_text':analyzed}
    # return HttpResponse('''''')
    return render(request,'punc.html',params)

def capitalizefirst(request):
    return HttpResponse('''''')

def newlinemove(request):
    return HttpResponse('''''')

def spaceremover(request):
    return HttpResponse('''''')

def charcount(request):
    return HttpResponse('''''')
