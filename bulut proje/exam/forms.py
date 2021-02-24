from .models import *
from django import forms

class createExamForm(forms.ModelForm):

    class Meta:
        model = Exam
        #fields = '__all__'
        exclude = ['owner_email']



        widgets = {
            'exam_name' : forms.TextInput(attrs={'placeholder' : 'Sınav Adı'}),
            'st_date' : forms.DateTimeInput(),
            'end_date' : forms.DateTimeInput(),
        }



class createQuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        #fields = '__all__'
        exclude = ['ques_no','exam_id']

        widgets = {

            'question' : forms.TextInput(attrs={'placeholder' : 'Soru'}),
            'A_choice' : forms.TextInput(attrs={'placeholder' : 'A Seçeneği'}),
            'B_choice' : forms.TextInput(attrs={'placeholder' : 'B Seçeneği'}),
            'C_choice' : forms.TextInput(attrs={'placeholder' : 'C Seçeneği'}),
            'D_choice' : forms.TextInput(attrs={'placeholder' : 'D Seçeneği'}),
            'E_choice' : forms.TextInput(attrs={'placeholder' : 'E Seçeneği'}),
        }



class answerExamForm(forms.ModelForm):

    class Meta :
        model = Answer
        exclude = ['owner_email','ques_id']

        widgets = {

            'answer' : forms.RadioSelect()
        }