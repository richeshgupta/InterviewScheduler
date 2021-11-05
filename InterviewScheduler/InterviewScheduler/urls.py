from users.views import *
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',InterviewPage,name='home'),
    path('test/',TestUI.as_view(),name='test'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
