"""secondpro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import blog.views
import mypage.views
from django.conf import settings #media 파일을 쓰려면 해야함 
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',blog.views.home, name="home"),
    #아무것도 없을 때 블로그 안에 있는 views.py의 파일안에 있는 home이라는 함수 가져오고 
    # 이름을 home이라고 짓겠다. 이렇게 하면 그냥 화면에 blogs로 지정해 놓은 텍스트가 뜸
    #blog안에 객체를 불러내기 위한 방법이 쿼리셋 메소드
    path('blog/<int:blog_id>', blog.views.detail,name="detail"),
    #계층적 url 형성하는데 효과적
    path('blog/new/',blog.views.new,name="new"),
    path('blog/create/',blog.views.create, name="create"),
    #작성된 내용을 만들어 줌, path를 추가한다고 해서 무조건 html을 띄워야 되는 건 아님, 이 path를 추가한 이유는
    #create함수를 실행하라는 의사를 전달하기 위함
    path('mypage/',mypage.views.mypage,name="mypage"),
    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)#path 설정하는 방법


#urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 이런 방식으로 해두됨