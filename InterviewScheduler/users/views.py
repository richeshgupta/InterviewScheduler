from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User
from .forms import InterviewForm
from django.views.generic import CreateView
from dateutil.parser import parse

import datetime
from django.conf import settings
from django.utils.timezone import make_aware



def ErrorPage(request,msg):
    return render(request,"users/error.html",{'msg':msg})

def InterviewPage(request):
    # user_obj = Participant.objects.all()
    users = User.objects.filter(is_staff=False,is_active=True)
    context = {'users':users}
    return render(request,"users/interviewpage.html",context)

class TestUI(CreateView):
    model = Interview
    fields = ['start_time','end_time']
    context_object_name='form'
    def form_valid(self,InterviewForm):
        return super().form_valid(InterviewForm)


def IsValidInterview(request):
    if(request.method=="GET"):
        return False
    else:
        return True


def GetOrCreateInterview(request):
    if request.method=="POST":
        from_date = request.POST.getlist('from_date')
        to_date = request.POST.getlist('to_date')
        # participants = request.POST.getlist('participants')
        if(len(participants)<2):
            return ErrorPage(request,"Less than 2 people can't create interview room")


        from_date = from_date[0]
        to_date = to_date[0]
        from_date = datetime.datetime.strptime(from_date, '%Y-%m-%d %H:%M:%S')
        to_date = datetime.datetime.strptime(to_date, '%Y-%m-%d %H:%M:%S')

        print(from_date)
        
        try:
            objs  = Interview.objects.filter(start_time = from_date,end_time = to_date)
        except:
            objs = Interview.objects.create(start_time=from_date,end_time = to_date,is_active = True)
            
        
        
    else:
        return render(request,"users/interviewpage.html",{})
    return render(request,"users/interviewpage.html",{})
