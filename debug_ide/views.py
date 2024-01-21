from django.shortcuts import render , HttpResponse

# Create your views here.

def hello(request):
    print(request.method)

    # return HttpResponse('helloWorld')
    return render(request, 'index.html', locals())
