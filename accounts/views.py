from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth import login as auth_login
# from .models import User
from django.contrib.auth import get_user_model

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:index')
    else:
        form = CustomUserCreationForm()

    context = {
        'form': form,
    }

    return render(request, 'accounts/form.html', context)


def login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('posts:index')

    else:
        form = CustomAuthenticationForm()

    context = {
        'form': form,
    }

    return render(request, 'accounts/form.html', context)


def profile(request, username):
    User = get_user_model()

    user_info = User.objects.get(username=username)

    context = {
        'user_info': user_info,
    }

    return render(request, 'accounts/profile.html', context)

from django.contrib.auth.decorators import login_required

@login_required
def follow(request, username):
    User = get_user_model()

    me = request.user
    you = User.objects.get(username=username)

    # 팔로잉이 이미 되어있는경우
    # if me in you.followers.all():
    if you in me.followings.all():
        me.followings.remove(you)
    # 팔로잉이 아직 안된경우
    else:
        me.followings.add(you)

    return redirect('accounts:profile', username=username)


