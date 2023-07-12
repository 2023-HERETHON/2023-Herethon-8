from django.shortcuts import render, get_object_or_404, redirect
from .models import Question
from django.utils import timezone

def question_view(request):
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list' : question_list}
    return render(request, 'questions.html', context)

def detail(request, question_id):
    question = Question.objects.get(id=question_id) #id에 해당하는 객체 get
    context = {'question' : question} #위에서 get한 question 객체를 text화
    return render(request, 'question_detail.html', context)

def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone)
    return redirect('qnas:detail', question_id=question_id)