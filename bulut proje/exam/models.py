from django.db import models
from home.models import user

# Create your models here.

class Exam(models.Model):
    owner_email = models.ForeignKey(user,on_delete=models.CASCADE,null=False,default=1)
    exam_name = models.CharField(max_length=60)
    st_date = models.DateTimeField(default='2021-02-20 20:00:00')
    end_date = models.DateTimeField(default='2021-02-20 20:00:00')

    def __int__(self):
        return self.id


class Question(models.Model) :
    class Meta:
        unique_together = (('ques_no','exam_id'),)
    ques_no = models.IntegerField(default=1)
    exam_id = models.ForeignKey(Exam,on_delete=models.CASCADE,default=1)
    question = models.CharField(max_length=100)
    A_choice = models.CharField(max_length=100)
    B_choice = models.CharField(max_length=100)
    C_choice = models.CharField(max_length=100)
    D_choice = models.CharField(max_length=100)
    E_choice = models.CharField(max_length=100)
    CHOICES = [('A','A'),('B','B'),('C','C'),('D','D'),('E','E')]
    trueChoice = models.CharField(max_length=20, choices=CHOICES, default=1)

    def __str__(self):
        return self.question

class Assignment(models.Model):
    partc_email = models.ForeignKey(user,on_delete=models.CASCADE,default=1,null=False)
    exam_id = models.ForeignKey(Exam,on_delete=models.CASCADE,default=1, null=False)
    joined_date = models.DateTimeField(auto_now_add=True)

    def __int__(self):
        return self.exam_id


class Answer(models.Model):
    owner_email = models.ForeignKey(user,on_delete=models.CASCADE,default=1)
    ques_id = models.ForeignKey(Question,on_delete=models.CASCADE,default=1)
    CHOICES = [('A','A'),('B','B'),('C','C'),('D','D'),('E','E')]
    answer = models.CharField(max_length=20, choices=CHOICES, default=1)

    def __str__(self):
        return self.answer

