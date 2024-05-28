from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def sign_up(request):
    if request.method == "GET":
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                context = {'user_name': user.username}
                return render(request, 'user_accounts/sign_up_success.html', context)

    context = {'form': form}
    return render(request, 'user_accounts/sign_up.html', context)


def sign_in(request):
    if request.method == "GET":
        form = AuthenticationForm()
    else:
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            pass_word = form.cleaned_data['password']
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                login(request, user)
                return redirect('home')

    context = {'form': form}
    return render(request, 'user_accounts/sign_in.html', context)


def sign_out(request):
    logout(request)
    context = {}
    return render(request, 'user_accounts/sign_out_success.html', context)
