from django.shortcuts import render
from .models import Mypage
# Create your views here.
def mypage(request):
    mypages=Mypage.objects

    return render(request,'mypage.html',{'mypages':mypages})
