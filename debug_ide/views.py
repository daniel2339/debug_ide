from django.shortcuts import render , HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib import auth

@ensure_csrf_cookie

# Create your views here.

def hello(request):
    print(request.method)

    # return HttpResponse('helloWorld')
    return render(request, 'index.html', locals())

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