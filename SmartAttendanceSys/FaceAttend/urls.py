from django.urls import path
from . import views


app_name = 'FaceAttend'
urlpatterns = [ path('',views.take_attendance,name='take_attendance'),
                path('do_attendance/',views.do_attendance, name='do_attendance'),
                path('login/',views.login,name='login')
                ]
