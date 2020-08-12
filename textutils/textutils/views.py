# Created my me
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index.html')
    #return HttpResponse('''<h1>Hello Abhinav Bhai!<h1> <a href="https://www.w3schools.com">Visit W3Schools.com!</a> ''')


def about(request):
    return HttpResponse("Age=19")

def analyze(request):
 data = request.GET.get('text', 'No text entered')

 remPunc = request.GET.get('removepunc', 'of')
 caps = request.GET.get('fullcaps', 'of')
 newLineRem = request.GET.get('newlineremover', 'of')
 spaceRem = request.GET.get('extraspaceremover', 'of')


 strr = data
 purpose = ""

 if remPunc == 'on':
  tempStr = ""
  puns = '''!@#$%^&*();'.,/:?>'''
  for i in data:
   if i not in puns:
    tempStr = tempStr + i
  params = {'purpose':'remove Punctuations' , 'answer':tempStr}
  strr = tempStr
  purpose += " | Remove Punctuations "
  # return render(request, 'analyze.html', params)
 if caps == 'on':
  print("2",strr)
  strr = strr.upper()
  params = {'purpose':'Caps' , 'answer':strr}
  purpose += "| Caps |"
  # return render(request, 'analyze.html', params)

 if newLineRem == 'on':
  tempStr=""
  for i in strr:
   if i != '\n':
    tempStr += i
  params = {'purpose':'New Line remove' , 'answer':tempStr}
  strr = tempStr
  purpose += "| remove new line "
  # return render(request, 'analyze.html', params)

 if spaceRem == 'on':
  tempStr = ""
  for index, ch in enumerate(strr):
   if not (strr[index] == " " and strr[index+1]==" "):
    tempStr += ch
  params = {'purpose':'spaces remove' , 'answer':tempStr}
  strr = tempStr
  purpose += "| Spaces remove |"

 params = {'purpose':purpose , 'answer':strr}

 if remPunc == 'on' or caps == 'on' or newLineRem == 'on' or spaceRem == 'on':
  return render(request, 'analyze.html', params)
 else:
  return HttpResponse('error hai bhai')



def capfirst(request):
    return HttpResponse("capitalize first")
def newlineremove(request):

    return HttpResponse("capitalize first")
def spaceremove(request):

    return HttpResponse("<h1>space remover</h1> <a href='/'>Back</a>")
def charcount(request):

    return HttpResponse("charcount ")
