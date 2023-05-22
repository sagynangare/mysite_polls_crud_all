from django import forms
from .models import Question, Choice
from django.utils import timezone

class QuestionForm(forms.ModelForm):
	question_text = forms.CharField(
							widget = forms.TextInput(attrs={
								'placeholder':'Enter a new question',
								'class':'form-control'
								}))
	pub_date = forms.DateTimeField(initial=timezone.now())

	class Meta:
		model=Question
		fields = '__all__'#['question_text','pub_date']

class ChoiceForm(forms.ModelForm):
	choice_text= forms.CharField(
							widget = forms.TextInput(attrs={
								'placeholder':'Enter a new choice',
								'class':'form-control'
								}))
	votes=forms.IntegerField(widget = forms.NumberInput(attrs={
				"placeholder":"Enter votes",
				"class":"form-control"}))

	class Meta:
		model=Choice
		fields = '__all__'


class UpForm(forms.Form):
	question_id=forms.IntegerField(widget = forms.NumberInput(attrs={
				"placeholder":"Enter Question ID",
				"class":"form-control"}))

	question_text = forms.CharField(
							widget = forms.TextInput(attrs={
								'placeholder':'Enter a new question',
								'class':'form-control'
								}))
	pub_date = forms.DateTimeField(initial=timezone.now())


class DelForm(forms.Form):
	question_id=forms.IntegerField(widget = forms.NumberInput(attrs={
				"placeholder":"Enter Question ID to delete question",
				"class":"form-control"}))
	