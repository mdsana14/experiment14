from django.urls import path
from .views import CustomLoginView, register, logout_view, about, contact, student_list

urlpatterns = [
    path('', student_list, name='student_list'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', register, name='register'),
    path('logout/', logout_view, name='logout'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
]
