from django.shortcuts import render
from .models import Questions, Brawlers
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    context = {}
    return render(request, 'articles/index.html', context)

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
        # 'question_img': question.image,
        'question_pk': question.pk,
        'question_ans1': question.answer1,
        'question_letter1': question.answer1_letter,
        'question_ans2': question.answer2,
        'question_letter2': question.answer2_letter,
        'mbti': mbti,
    }
    return JsonResponse(data)

def result(request, mbti):
    brawlers = Brawlers.objects.all()
    
    # first = {}
    # second = {}
    # third = {}
    # fourth = {}
    # result = ''
    
    # first['I'] = mbti.count('I') # first['I'] == key / mbti.count('I') == value / ex: {'I': 1, 'E': 2}
    # first['E'] = mbti.count('E') # first['E'] == key / mbti.count('E') == value / ex: {'I': 1, 'E': 2}
    # key = max(first, key=first.get) # key = max(dict_name, key=dict_name.get)
    # result += key # result += max_value를 가지는 key(ex: 'E')
    
    # second['S'] = mbti.count('S')
    # second['N'] = mbti.count('N')
    # key = max(second, key=second.get)
    # result += key
    
    # third['T'] = mbti.count('T')
    # third['F'] = mbti.count('F')
    # key = max(third, key=third.get)
    # result += key

    # fourth['P'] = mbti.count('P')
    # fourth['J'] = mbti.count('J')
    # key = max(fourth, key=fourth.get)
    # result += key
    
    result = 'ESTP'

    for brawler in brawlers:
        if brawler.mbti == result:
            result_brawler = Brawlers.objects.get(mbti=brawler.mbti)
            image = result_brawler.image
            break
        
    context = {
        'result_brawler': result_brawler,
        'image': image,
    }
    return render(request, 'articles/result.html', context)
