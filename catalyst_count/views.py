from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return redirect('upload/')

def login(request):
    if not request.user.is_authenticated:
        return render(request, 'account/login.html')
    else:
        return redirect('upload/') 
