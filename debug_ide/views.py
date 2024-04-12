from django.shortcuts import render , HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib import auth
from django.contrib.auth.models import User

@ensure_csrf_cookie

# Create your views here.

def signup(request):

    #Html / Javascript
    #   確認：使用者名稱
    #   確認：密碼一致
    #   確認：Email
    #   確認：同意條款
    #   ajax送出：註冊資料
    #   跳轉：登入頁

    # views.py
    #   接收：帳號(Email)
    #   接收：密碼
    #   接收：使用者名稱
    #   建立：新使用者


    # user = User.objects.create_user("")

    return render(request, 'signup.html',locals())

def hello(request):
    print(request.method)

    if request.user.is_authenticated:
        return render(request, 'index.html',locals())
    else:
        return HttpResponseRedirect('/debug_ide/login')

    # return HttpResponse('helloWorld')
    # return render(request, 'index.html', locals())

def signupData(request):
    return


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/debug_ide/')


def login(request):

    if request.user.is_authenticated:
        return HttpResponseRedirect('/debug_ide/')


    username = request.POST.get('email','')
    password = request.POST.get('password','')
    user = auth.authenticate(username=username, password=password)

    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect('/debug_ide/')
    else:
        return render(request, 'sign_in_up.html',locals())

    # return render(request,'sign_in_up.html',locals())