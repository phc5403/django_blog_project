from django.contrib import admin
from .models import Blog # 같은 폴더 위치에 있는 models 라는 파일에, Blog 라는 클래스를 가지고 온다.

# Register your models here.

# admin이라는 site에 Blog 클래스를 등록한다.
admin.site.register(Blog)