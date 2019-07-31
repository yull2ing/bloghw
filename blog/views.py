from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from .models import Blog

def home(request):
    blogs=Blog.objects #쿼리셋 #메소드
    return render(request,'home.html',{'blogs':blogs})
    
def detail(request,blog_id):
    blog_detail=get_object_or_404(Blog,pk=blog_id)#이용자가 원한 몇 번 블로그 객체를 변수 안에 담음
    return render(request,'detail.html',{'blog':blog_detail})

def new(request):#new.html을 띄워주는 함수 
    return render(request,'new.html')

def create(request): #입력받은 내용을 데이터베이스에 넣어주는 함수 
    blog=Blog() #blog라는 클래스로 부터 좌변에 있는 blog 객체 하나 생성
    blog.title=request.GET['title'] #title에서 입력한 내용을 가져와서 blog.title이라는 변수에 넣어준다
    blog.body=request.GET['body']
    blog.pub_date=timezone.datetime.now()#블로그를 작성한 시점을 넣어주는 함수 (상당히 자주 쓰는 함수)
    blog.save() #데이터가 들어간 객체를 데이터 베이스에 저장해라
    #객체.delete() 데이터베이스로부터 객체를 지워라 
    return redirect('/blog/'+str(blog.id))#위를 다 처리한 담에 괄호 안에 있는 url로 이동
    #blog.id는 정수형이기 때문에 str 써서 문자형으로 형 변환
    #redirect와 render의 차이 ->redirect는 괄호 안에 다른 url을 넣을 수 있음 ex)google.com