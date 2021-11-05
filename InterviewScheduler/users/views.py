from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User
from .forms import InterviewForm
from django.views.generic import CreateView

def ErrorPage(request,msg):
    return render(request,"users/error.html",{'msg':msg})
# Create your views here.
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


