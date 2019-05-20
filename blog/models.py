from django.db import models

# Create your models here.
class Blog(models.Model):
    #제목, 시간, 내용
    title=models.CharField(max_length=200)
    pub_date= models.DateTimeField('date published')
    body=models.TextField()

    def __str__(self):
        return self.title

    def summary(self):  #본문 100 글자 상한선
        return self.body[:100] #slicing(리스트 자르기)
        