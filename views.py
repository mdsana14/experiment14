from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from .models import Student
from .forms import StudentForm

class CustomLoginView(LoginView):
    template_name = 'studentapp/login.html'

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'studentapp/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def about(request):
    return render(request, 'studentapp/about.html')

def contact(request):
    return render(request, 'studentapp/contact.html')

@login_required
def student_list(request):
    students = Student.objects.all()
    return render(request, 'studentapp/student_list.html', {'students': students})
