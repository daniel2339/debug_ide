from django.shortcuts import render , HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import openai
from django.conf import settings
from django.http import JsonResponse
import os
import logging
openai.api_key = settings.OPENAI_API_KEY
logger = logging.getLogger(__name__)
@ensure_csrf_cookie

# Create your views here.

def signup(request):


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
    # 1.收到前端傳來的資料
    # 2.建立使用者資料到DB
    # 3.如果建立成功，回傳訊息至前端
    # 4.如果建立失敗，回傳訊息至前端

    username = request.POST.get('username','')
    password = request.POST.get('password','')
    email = request.POST.get('email','')
    # 可加密碼檢查

    # 可加傳入資料檢查

    try:
        user = User.objects.create_user(username,email,password)
        user.save()

        return JsonResponse({'msg':'ok'})
    except Exception as e:
        print(e)
        return JsonResponse({'msg':'NOT OK'})


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

# def userFeedback(request):

#     feedback = request.POST.get('feedback','')

#     if request.user.is_authenticated:
#         return HttpResponse('OK')
#         print()
#     else:
#         return HttpResponse('helloWorld')



def question(request):
    return render(request, 'question.html')

@csrf_exempt
def debug_code(request):
    if request.method == "POST":
        try:
            body = json.loads(request.body)
            content = body.get("code")
            request_type = body.get("type", "general")

            if not content:
                return JsonResponse({"error": "No content provided"}, status=400)

            if request_type == "code":
                prompt = f"只需要回覆我修正後的程式碼並排版完整，只要code不用任何說明 這段文字: (如果正確則回答 此code沒有錯誤)\n\n{content}"
            elif request_type == "general":
                prompt = f"這是使用者的代碼及相關問題，請根據這些資訊回答問題，只需回覆錯誤的那行就好，如果使用者問的問題與該題無關，就回答使用者的問題即可：\n\n{content}"
            elif request_type == "solution":
                prompt = f"請幫助我解釋這個題目的解題思路，給出簡單明瞭的步驟和建議：\n\n{content}"
            else:
                prompt = content

            # 使用 OpenAI API 回答問題
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "你是一個程式碼偵錯助手。" if request_type == "code" else "你是一個全能助理。"},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=1000,
                temperature=0.5
            )

            reply = response.choices[0].message['content'].strip()
            return JsonResponse({"reply": reply})

        except openai.error.OpenAIError as api_error:
            # 處理 OpenAI API 相關的錯誤
            print(f"OpenAI API error: {str(api_error)}")
            return JsonResponse({"reply": "這是模擬的回應，因為 API 配額已用完。"})

        except Exception as e:
            # 捕捉其他一般錯誤
            print(f"Error occurred while processing the request: {str(e)}")
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request method"}, status=400)
