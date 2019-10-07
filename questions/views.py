from django.shortcuts import render, redirect
from .models import Question
# Create your views here.


def index(request):
    questions = Question.objects.all()  # 데이터 베이스에 있는 전체 정보를 불러옴
    context = {
        'questions': questions
    }
    return render(request, 'index.html', context)  # 그 정보를 딕셔너리에 담아서 인덱스에 넘겨줌


def detail(request, id):
    question = Question.objects.get(id=id)
    context = {
        'question': question,
    }
    return render(request, 'detail.html', context)


def create(request):
    if request.method == "POST":
        content = request.POST.get('content')
        Question.objects.create(content=content)

        return redirect('questions:index')  # 인덱스로 다시 보내준다.
    else:
        return render(request, 'form.html')
