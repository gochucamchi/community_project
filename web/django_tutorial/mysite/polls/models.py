import datetime

from django.db import models
from django.utils import timezone
# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)  #문자열 타입(크기 200)
    pub_date = models.DateTimeField('date published') #시간 타입을 가지고 있음 
    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1) #현재의 시간에서 하루를 차감한 어제의 데이터와 저장된 데이터중에 저장된 데이터가 크거나 같은지 확인한다 
    
    #->저장된 날자가 어제이후인지 확인한다 
class Choice(models.Model):
    Question = models.ForeignKey(Question, on_delete=models.CASCADE) #외래키 -> Question이라는 데이터 모델을 참조하겠다는 뜻, CASCADE는 데이터가 변하면 같이 변한다는 의미
    choice_text = models.CharField(max_length= 200)
    votes = models.IntegerField(default=0) #인트형 데이터 타입
    def __str__(self):
        return self.choice_text

#데이터 모델은 Question과 choice가 있다
#question_text는 질문 내용
#pub_date는 질문 날자
#question은 선택지에 해당하는 질문
#votes 투표수