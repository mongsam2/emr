from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserForm

# Create your views here.
def home(request):
    return render(request, 'common/home.html')

def start(request):
    return render(request, 'common/start.html')

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password) # 사 용자 인 증
            login(request, user) # 로 그 인
            return redirect('common:start')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})

