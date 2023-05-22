from django.shortcuts import render, get_object_or_404, redirect

from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse
from .forms import QuestionForm, ChoiceForm, UpForm, DelForm
from django.contrib import messages
from django.utils import timezone

def index(request):
	question_list = Question.objects.all()
	#result = "<br>".join([q.question_text for q in question_list])
	#return HttpResponse(result)
	context = {"latest_question":question_list}
	return render(request,"polls/index.html", context)

def detail(request, question_id):
	que = get_object_or_404(Question, pk=question_id)
	return render(request,"polls/detail.html", {'question':que})

def vote(request,question_id):
	que = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = que.choice_set.get(pk=request.POST['choice'])

	except (KeyError, Choice.DoesNotExist):
		return render(request,"polls/detail.html",
			{
			'question':que,
			'error_message':"You didn't select a choice"
			},)
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse("polls:detail", args=(que.id, )))

def add_question(request):
	if request.method=='POST':
		question=QuestionForm(request.POST)
		if question.is_valid():
			question.save()
			messages.info(request, "Question Added Successfully!")
			return HttpResponseRedirect(reverse("polls:index"))
		else:
			messages.info(request, "Invalid data")
			return HttpResponseRedirect(reverse("polls:add_question"))
	else:
		question=QuestionForm()
		return render(request, "polls/add_question.html",{'question':question})


def add_choice(request,question_id):
	if request.method=='POST':
		chform=ChoiceForm(request.POST)
		if chform.is_valid():
			ch_text=request.POST.get('choice_text','')
			vts=request.POST.get('votes',0)
			ques=get_object_or_404(Question, pk=question_id)
			ques.choice_set.create(choice_text=ch_text, votes=vts)
			ques.save()
			messages.info(request, "Name updated successfully")
			return redirect(reverse("polls:detail", args=(question_id, )))
		else:
			messages.info(request,"Invalid Information")
			return redirect(reverse("polls:add_choice"))
	else:
		chform=ChoiceForm()
		return render(request, "polls/add_choice.html",{'choice':chform})

#1) Add new view to Update  a given question and choices

def update_question(request):
	if request.method=='POST':
		upform=UpForm(request.POST)
		if upform.is_valid():
			qid=request.POST.get('question_id',1)
			qtext=request.POST.get('question_text','')
			pdate=request.POST.get('pub_date', timezone.now())
			ques=get_object_or_404(Question, pk=qid)
			ques.question_text=qtext
			ques.pub_date=pdate
			ques.save()
			return redirect(reverse("polls:index"))
		else:
			messages.info(request,"Invalid Information")
			return redirect(reverse("polls:update_question"))
	else:
		upform=UpForm()
		return render(request, "polls/update.html",{'upform':upform})

#Add new view to delete selected question
def delete_question(request):
	if request.method=='POST':
		delform=DelForm(request.POST)
		if delform.is_valid():
			qid=request.POST.get('question_id',1)
			ques=get_object_or_404(Question, pk=qid)
			ques.delete()
			return redirect(reverse("polls:index"))
		else:
			messages.info(request,"Invalid Information")
			return redirect(reverse("polls:delete_question"))
	else:
		delform=DelForm()
		return render(request, "polls/delete.html",{'delform':delform})








"""
Task-
1) Add new view to Update  a given question and choices
2) Add new view to delete selected question

"""