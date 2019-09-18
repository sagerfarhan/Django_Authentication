from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    count = User.objects.count()
    return render(request, 'authenapp/index.html', {
        'count': count
    })


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = UserCreationForm()
    return render(request,'registration/signup.html', {
        'form': form
    } )

@login_required
def secret_page(request):
    return render(request, 'secret_page.html')




