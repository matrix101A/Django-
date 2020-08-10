# Created my me
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index.html')
    #return HttpResponse('''<h1>Hello Abhinav Bhai!<h1> <a href="https://www.w3schools.com">Visit W3Schools.com!</a> ''')
def about(request):
    return HttpResponse("Age=19")
def removepunc(request):
    #get the text
    djtext= print(request.GET.get('text','default'))
    print(djtext)
    #analyze the text
    
    return HttpResponse("remove punc")
def capfirst(request):
    return HttpResponse("capitalize first")
def newlineremove(request):

    return HttpResponse("capitalize first")
def spaceremove(request):

    return HttpResponse("<h1>space remover</h1> <a href='/'>Back</a>")
def charcount(request):

    return HttpResponse("charcount ")
