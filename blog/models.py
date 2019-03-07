from django.db import models

# Create your models here.

class Blog(models.Model):
    # 이하의 내용이 admin 페이지에서 add blog 페이지의 양식을 결정한다.
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    
    def __str__(self):
        return self.title
        
    # 만약 def summary(Blog)라면, return은 Blog 클래스에 정의된 body에서 100글자만 출력하라는 의미가 된다.
    def summary(self):
        # 100글자 까지만 출력.
        return self.body[:100] 