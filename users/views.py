from django.shortcuts import render, redirect, get_object_or_404
from allauth.account.forms import LoginForm, SignupForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.views.decorators.http import require_POST
from .forms import AddUserForm
from django.contrib import messages


@login_required(login_url="/login/")
def Users(request):
    User = get_user_model()
    users = User.objects.all()
    #users = User.objects.all()
    return render(request, 'users.html', {'users': users})

@require_POST
@login_required(login_url="/login/")
def add_user(request):
    User = get_user_model()
    users = User.objects.all()
    if request.method == 'POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'New user added')
            #return redirect('users:add_user', {'form': form, 'users': users})  # Redirect to user list view or any other page after successful submission
            return render(request, 'users.html', {'form': form, 'users': users})
    else:
        form = AddUserForm()
    
    return render(request, 'users.html', {'form': form, 'users': users})
    #return redirect('users')

@require_POST
@login_required(login_url="/login/")
def delete_user(request, user_id):
    User = get_user_model()
    user = get_object_or_404(User, pk=user_id)
    user.delete()
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})


class LoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['login'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'class': 'form-control'})
        self.fields['login'].label = 'Username'
