from django.shortcuts import render

# Create your views here.
def welcome(request):
    context = {}
    return render(request, 'articles/welcome.html', context)

def result(request):
    context = {}
    return render(request, 'articles/result.html', context)

def question(request):
    context = {}
    return render(request, 'articles/question.html', context)