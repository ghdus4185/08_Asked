from django.shortcuts import render, redirect
from .models import Question, Answer
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


def answer_create(request, question_id):
    if request.method == "POST":
        content = request.POST.get('content')
        question = Question.objects.get(id=question_id)

        Answer.objects.create(content=content, question=question)

        return redirect('questions:detail', question_id)
    else:
        pass


def answer_delete(request, question_id, answer_id):
    answer = Answer.objects.get(id=answer_id)
    answer.delete()

    return redirect('questions:detail', question_id)
