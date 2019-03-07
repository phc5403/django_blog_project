from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.utils import timezone # timezone 패키지 사용.
from .models import Blog # views.py파일에 models.py파일에 있는 Blog 클래스를 import

# Create your views here.

def blog(request): # 원래 home
    # model로 부터 객체 목록을 전달 받을 수 있다. (=쿼리셋) -> Method(기능들을 표시해줄수있는 방법)
    blogs = Blog.objects
    
    # views.py 파일의 blogs라는 템플릿 변수를 사용할때 blogs라고 네이밍해서 가져오겠다.
    return render(request, 'blog.html', {'blogs' : blogs})

# detail 함수는 request와 blog_id를 함께 받아 해당 데이터를 넘겨준다. 그러면 모델에서 id를 기준으로 데이터를 가져와 있으면 보여주고 없으면 404에러를 띄운다. id값은 만든적이 없어도 django가 기본적으로 만들어 준다.
def detail(request, blog_id):
    # object를 가져온다, 없을경우 404 에러를 띄운다. 인자는 (대문자로시작하는 모델명, 불러올 blog 게시글의 id값) 
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog' : blog_detail})
 
def create(request): # create.html을 띄워주는 함수. 
    return render(request, 'create.html')
   
def new(request): # 글 쓰기
    blog = Blog()
    # title은 create.html input 태그의 name이다. 
    blog.title = request.GET['title']
    # body은 create.html textarea 태그의 name이다.
    blog.body = request.GET['body']
    # 입력한 시간이 자동으로 넘어가게 한다 = timezone 패키지 사용.
    blog.pub_date = timezone.datetime.now()
    blog.save()
    # redirect : 요청이 들어오면 인자의 URL로 보낸다.
    return redirect('/blog/' + str(blog.id))