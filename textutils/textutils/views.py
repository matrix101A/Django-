# Created my me
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
 data = request.POST.get('text', 'No text entered')

 remPunc = request.POST.get('removepunc', 'of')
 caps = request.POST.get('fullcaps', 'of')
 newLineRem = request.POST.get('newlineremover', 'of')
 spaceRem = request.POST.get('extraspaceremover', 'of')


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
  for i in range(len(strr)):
   print(strr[i])
   if strr[i] is not '\n' and strr[i] is not '\r':
    tempStr += strr[i]
  params = {'purpose':'New Line remove' , 'answer':tempStr}
  strr = tempStr
  purpose += "| remove new line "
  # return render(request, 'analyze.html', params)

 if spaceRem == 'on':
  tempStr = ""
  for index, ch in enumerate(strr):
   if not (index<len(strr)-1 and strr[index] == " " and strr[index+1]==" "):
    tempStr += ch
  params = {'purpose':'spaces remove' , 'answer':tempStr}
  strr = tempStr
  purpose += "| Spaces remove |"

 params = {'purpose':purpose , 'answer':strr}

 if remPunc == 'on' or caps == 'on' or newLineRem == 'on' or spaceRem == 'on':
  return render(request, 'analyze.html', params)
 else:
  return HttpResponse('error hai bhai')

