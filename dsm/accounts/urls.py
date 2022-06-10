from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('register/', views.my_form,name='register'),
    path('login/', views.login,name='login'),
    path('planSelection/', views.planSelection,name='planSelection'),
    path('MainPage/', views.dashboard,name='MainPage'),
    path('TeacherInfo/', views.TeacherInfo,name='TeacherInfo'),
    path('UserPlan/', views.UserPlan,name='UserPlan'),
    path('MarkAttendance/', views.MarkAttendance,name='MarkAttendance'),
    path('Attendance/', views.Attendance,name='Attendance'),
]