from django.db import models

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=200)
    pub_date=models.DateTimeField('date published')
    body=models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]
        #more...이 되도록 하기 위한 함수 설정 
        #[:100] 100글자 이상이 되었을 떄 return이 되도록
 