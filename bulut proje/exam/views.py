from django.shortcuts import render,HttpResponseRedirect
from .forms import *
from .models import *

# Create your views here.

def createExamView(request):

    form = createExamForm(request.POST or None)


    if form.is_valid():
        Exam.objects.create(exam_name=request.POST['exam_name'],
                            st_date=request.POST['st_date'],
                            end_date=request.POST['end_date'],
                            owner_email_id=request.session['email'])

        id = Exam.objects.all().last().id
        return HttpResponseRedirect('/Egitmen/createExam/'+str(id)+'/question/1')

    return render(request,"exam.html" , {"form":form})

def createQuestionView(request,id,id2):
    form = createQuestionForm(request.POST or None)

    if form.is_valid():
        Question.objects.create(ques_no=id2,
                                question=request.POST['question'],
                                A_choice=request.POST['A_choice'],
                                B_choice=request.POST['B_choice'],
                                C_choice=request.POST['C_choice'],
                                D_choice=request.POST['D_choice'],
                                E_choice=request.POST['E_choice'],
                                trueChoice=request.POST['trueChoice'],
                                exam_id_id=id)

        id2 = id2+1
        return HttpResponseRedirect('/Egitmen/createExam/'+str(id)+'/question/'+str(id2))

    return render(request,"question.html" , {"form":form , "ques_no" : id2 , "exam_id" : id})