from django.shortcuts import render
from .models import Questions, Choices

# Create your views here.
def welcome(request):
    context = {}
    return render(request, 'articles/welcome.html', context)

def result(request):
    choice = Choices()
    mbti = ''
    if choice.I_choice > choice.E_choice:
        mbti += 'I'
    else:
        mbti += 'E'
        
    if choice.S_choice > choice.N_choice:
        mbti += 'S'
    else:
        mbti += 'N'

    if choice.T_choice > choice.F_choice:
        mbti += 'T'
    else:
        mbti += 'F'

    if choice.P_choice > choice.J_choice:
        mbti += 'P'
    else:
        mbti += 'J'
        
    final_mbti = Brawlers.mbti(mbti)
    context = {
        'mbti': mbti,
    }
    return render(request, 'articles/result.html', context)

def question(request):
    context = {}
    return render(request, 'articles/question.html', context)