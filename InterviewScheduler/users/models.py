from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# from django.utils.timezone import localtime 
from django.utils.dateparse import parse_datetime


class Interview(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default = False)
    # timezone = models.
    def __str__(self):
        # print(localtime.__dir__)
        return str(self.start_time) + " : " + str(self.end_time)

class Participant(models.Model):
    resume = models.FileField(upload_to="resume",blank = True)
    parent_user = models.OneToOneField(User, on_delete=models.CASCADE)
    interview = models.ManyToManyField(Interview)
    def __str__(self):
        super_user_obj = self.parent_user
        print(super_user_obj)
        return str(super_user_obj)


