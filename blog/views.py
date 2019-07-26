from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog
from .forms import BlogPost
# Create your views here.

def home(request):
    blogs=Blog.objects
    return render(request, 'home.html', {'blogs': blogs})

def detail(request, blog_id):
    details=get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html',{'details':details})

def new(request):
    return render(request, 'new.html')

def create(request):
    blog=Blog() #블로그 객체 생성
    blog.title=request.GET['title'] #입력받은 내용을 변수 안에 저장
    blog.body=request.GET['body'] 
    blog.pub_date=timezone.datetime.now() #블로그 작성한 시점을 넣어주는 함수
    blog.save() #객체를 DB에 저장
    return redirect('/blog/'+ str(blog.id)) #str(): 문자열로 형변환, url+문자열

def blogpost(request):
    if request.method =='POST':
        form = BlogPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date=timezone.now()
            post.save()
            return redirect('home')
    else:
        form = BlogPost()
        return render(request,'new.html',{'form':form})