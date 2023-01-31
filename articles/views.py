from django.shortcuts import render
from .models import Questions
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def welcome(request):
    context = {}
    return render(request, 'articles/welcome.html', context)

@csrf_exempt
def question(request):
    question = Questions.objects.get(pk=1)
    mbti = ''
    context = {
        'question': question,
    }
    return render(request, 'articles/question.html', context)

@csrf_exempt
def ajax(request):
    pk = request.POST.get('pk')
    letter = request.POST.get('letter')
    mbti = request.POST.get('mbti')
    pk = int(pk) + 1
    mbti += letter
    question = Questions.objects.get(pk=pk)
    data = {
        'question': question.question,
        'question_pk': question.pk,
        'question_ans1': question.answer1,
        'question_letter1': question.answer1_letter,
        'question_ans2': question.answer2,
        'question_letter2': question.answer2_letter,
        'mbti': mbti,
    }
    return JsonResponse(data)

def result(request):
    
    return render(request, 'articles/result.html')
