from django.shortcuts import render,HttpResponseRedirect
from .forms import *
from .models import user
from exam.models import Exam,Question,Answer,Assignment
import datetime
from exam.forms import answerExamForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


# Create your views here.

def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        if(user.objects.filter(email=email).exists()):

            if(user.objects.get(email=email).password == password):

                if(user.objects.get(email=email).type == "egitmen"):
                    request.session['email'] = email

                    return HttpResponseRedirect ('/Egitmen')

                else :
                    request.session['email'] = email

                    return HttpResponseRedirect ('/Ogrenci')

    return render(request, "login.html", {"form": form})

def signup_view(request):
    form = SignupForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")

    return render(request,"Signup.html" , {"form":form})

def home_egitmen_view(request):

    gecmis_sinavlar = []
    gelecek_sinavlar = []

    tum_sinavlar = Exam.objects.filter(owner_email=request.session['email'])
#    print(tum_sinavlar[0].end_date.strftime('%Y-%m-%d %H:%M:%S,%f'))
#   print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S,%f'))
    for sinav in tum_sinavlar:
        if(sinav.end_date.strftime('%m-%d-%Y %H:%M:%S,%f')
                < datetime.datetime.now().strftime('%m-%d-%Y %H:%M:%S,%f')):
            gecmis_sinavlar.append(sinav)
        else:
            gelecek_sinavlar.append(sinav)
#    print(gecmis_sinavlar)
#    print(gelecek_sinavlar)
    f_name = user.objects.get(email=request.session['email']).f_name
    l_name = user.objects.get(email=request.session['email']).l_name
    return render(request,"Egitmen.html", {"fname" : f_name  , "lname" : l_name, "gelecek_sinavlar" : gelecek_sinavlar, "gecmis_sinavlar" : gecmis_sinavlar})

def home_ogrenci_view(request):
    yaklasan_sinavlar = []
    girilebilir_sinavlar = []

    tum_sinavlar = Exam.objects.all()



    for sinav in tum_sinavlar:
        if(sinav.end_date.strftime('%m-%d-%Y %H:%M:%S,%f') > datetime.datetime.now().strftime('%m-%d-%Y %H:%M:%S,%f') and
                (sinav.st_date.strftime('%m-%d-%Y %H:%M:%S,%f') <= datetime.datetime.now().strftime('%m-%d-%Y %H:%M:%S,%f'))):
            girilebilir_sinavlar.append(sinav)
        elif(sinav.st_date.strftime('%m-%d-%Y %H:%M:%S,%f') >= datetime.datetime.now().strftime('%m-%d-%Y %H:%M:%S,%f')):
            yaklasan_sinavlar.append(sinav)
#   print(girilebilir_sinavlar)
#   print(yaklasan_sinavlar)

    #katildigim_sinavlar = Assignment.objects.filter(partc_email = request.session['email'])


    f_name = user.objects.get(email=request.session['email']).f_name
    l_name = user.objects.get(email=request.session['email']).l_name
    return render(request,"Ogrenci.html", {"fname" : f_name  , "lname" : l_name , "aktif_sinavlar" : girilebilir_sinavlar , "yaklasan_sinavlar" : yaklasan_sinavlar })

def detailView(request,id):
    f_name = user.objects.get(email=request.session['email']).f_name
    l_name = user.objects.get(email=request.session['email']).l_name
    sorular = Question.objects.filter(exam_id=id)
    sinav_adi  = Exam.objects.get(id=id).exam_name
    return render(request,"detail.html", {"sorular" : sorular , "exam_name" : sinav_adi ,"fname" : f_name  , "lname" : l_name})

def joinExam(request,id,id2):


    form = answerExamForm(request.POST or None)

    f_name = user.objects.get(email=request.session['email']).f_name
    l_name = user.objects.get(email=request.session['email']).l_name
    soru_sayisi = Question.objects.filter(exam_id=id).count()

    if (id2 > soru_sayisi):
        Assignment.objects.create(exam_id_id= id,
                              partc_email_id= request.session['email'])

        return HttpResponseRedirect('/Ogrenci')

    soru = Question.objects.filter(exam_id=id).get(ques_no=id2).question
    A = Question.objects.filter(exam_id=id).get(ques_no=id2).A_choice
    B = Question.objects.filter(exam_id=id).get(ques_no=id2).B_choice
    C = Question.objects.filter(exam_id=id).get(ques_no=id2).C_choice
    D = Question.objects.filter(exam_id=id).get(ques_no=id2).D_choice
    E = Question.objects.filter(exam_id=id).get(ques_no=id2).E_choice

    if form.is_valid():
        Answer.objects.create(owner_email_id= request.session['email'],
                            ques_id_id= Question.objects.filter(exam_id=id).get(ques_no=id2).id,
                            answer=request.POST['answer'])
        id2 = id2 +1

        return HttpResponseRedirect('/Ogrenci/joinExam/'+str(id)+'/question/' +str(id2))


    return render(request,"joinExam.html", { "form" : form ,"fname" : f_name  , "lname" : l_name , "soru_sayisi" : soru_sayisi , "ques_no" : id2
                                             ,"soru" : soru, "A" : A, "B" : B, "C" : C , "D" : D , "E" : E})