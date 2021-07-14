# I have ceated this file - Omkar

from django.http import HttpResponse
from django.shortcuts import render
import string


def index(request):
    return render(request, 'index.html')


def textOperation(request):
    text = request.POST.get('text', 'default')
    rempunc = request.POST.get('rempunc', 'off')
    capi = request.POST.get('capi', 'off')
    newl = request.POST.get('newl', 'off')
    espace = request.POST.get('espace', 'off')
    operationDic = {'rempunc': rempunc,
                    'capi': capi, 'newl': newl, 'espace': espace}
    analyzed_text = ''
    purpose = ''
    for key, value in operationDic.items():
        if str(value) == 'on':
            if str(key) == 'rempunc':
                temVar = ''
                purpose = purpose + 'rempunc'
                punctuations = string.punctuation
                for char in text:
                    if char not in punctuations:
                        temVar = temVar + char
                text = temVar
            elif str(key) == 'capi':
                temVar = ''
                purpose = purpose + 'capi'
                for char in text:
                    temVar = temVar + char.upper()
                text = temVar
            elif str(key) == 'newl':
                temVar = ''
                purpose = purpose + 'newl'
                for char in text:
                    if char != '\n' and char != '\r':
                        temVar = temVar + char
                text = temVar
            elif str(key) == 'espace':
                temVar = ''
                purpose = purpose + 'espace'
                for index, char in enumerate(text):
                    if not(text[index] == ' ' and text[index + 1] == ' '):
                        temVar = temVar + char
                text = temVar
            else:
                return HttpResponse('Error. Please click on checkbox.')

    analyzed_text = text
    parameter = {'purpose': purpose,
                 'analyzed_text': analyzed_text}
    return render(request, 'analyze.html', parameter)
