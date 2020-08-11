# Created my me
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index.html')
    #return HttpResponse('''<h1>Hello Abhinav Bhai!<h1> <a href="https://www.w3schools.com">Visit W3Schools.com!</a> ''')


def about(request):
    return HttpResponse("Age=19")

def analyze(request):

    #get the text
    djtext= request.GET.get('text','default')
    removepunc=request.GET.get('removepunc','off')
    fullcaps=request.GET.get('fullcaps','off')
    newlineremover=request.GET.get('newlineremover','off')
    extraspaceremover=request.GET.get('extraspaceremover','off')

    #analyze the text
    analyzed = djtext

    if removepunc=='on':
        analyzed = ""
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose':'Removed Punctuations', 'analyzed_text':analyzed}
        return render(request,'analyze.html',params)

    elif (fullcaps == "on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()

        params = {'purpose': 'Changed to upper case ', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif newlineremover=="on":
        analyzed=""
        for char in djtext:
            if(char!="\n"):
                analyzed=analyzed+char

    elif extraspaceremover == "on":
        analyzed = ""
        for index,char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyzed+=char

        params = {'purpose': 'Removed new line', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    else:
      return HttpResponse(analyzed)




def capfirst(request):
    return HttpResponse("capitalize first")
def newlineremove(request):

    return HttpResponse("capitalize first")
def spaceremove(request):

    return HttpResponse("<h1>space remover</h1> <a href='/'>Back</a>")
def charcount(request):

    return HttpResponse("charcount ")
