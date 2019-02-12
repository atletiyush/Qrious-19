from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

# Create your views here.


def home(request):
    if(request.method == 'POST'):
        return redirect('/accounts/google/login')
    return render(request, 'index.html')


def loading(request):
    return render(request, 'loader.html')


def roulette(request):
    return render(request, 'roulette.html')


def l_out(request):
    logout(request)
    return redirect('/')


def quiz(request, filename):
    print("This function.")
    return render(request, filename)


def postanswer(request, filename):
    if request.method == 'POST':
        print(request.POST)
    return HttpResponse('')

def question_details(request):
    data_get = json.loads(request.body.decode('utf-8'))
    number=data_get["reality_number"]  #specify name of your choice in place of reality_number
    questiondata=[]
    if number=='1':
        Questionlist=Question.objects.filter(reality_type="magic")
    elif number=='2':
        Questionlist=Question.objects.filter(reality_type="robotics")
    elif number=='3':
        Questionlist=Question.objects.filter(reality_type="mythology")
    elif number=='4':
        Questionlist=Question.objects.filter(reality_type="gaming")
    for questionlist in Questionlist:
                    question_list={}
                    question_list["queslist"]={'question':questionlist.question,'choice1':questionlist.choice1,'choice2':questionlist.choice2,
                                    'choice3':questionlist.choice3,'choice4':questionlist.choice4,'correct_choice':questionlist.correct_choice}
                    questiondata.append(question_list)

    def leaderboard_view(request):
        data_get=json.loads(request.body.decode('utf-8'))
   data = []
   leaderboard = Userdata.objects.order_by('score').reverse()[:10]
   for user in leaderboard:

      user_details = {}
      user_details["details"] = {"name": user.bits_id,
                                 "score": user.score}



      data.append(user_details)
      obj=Userdata.objects.get(bits_id=data_get['email'])
      my_details={}
      my_details["details"] = {"name": obj.bits_id,
                                 "score": obj.score}
      data.append(my_details)
   return JsonResponse(data, safe=False)
