from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect

# Create your views here.
def user_login(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('frontpage')
        
        else:
            #if login failed
            return render(request, 'useraccounts/login_failed.html')

def user_logout(request):
    logout(request)
    return redirect('frontpage')

def user_register(request):
    context = {}
    if request.method == 'POST':
        user = User()
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.first_name = request.POST.get('firstname')
        user.last_name = request.POST.get('lastname')
        user.set_password(request.POST.get('password'))
        
        if User.objects.filter(username=user.username).exists():
            context['username_taken'] = True
            return render(request, 'useraccounts/register_failed.html', context)
        
        elif User.objects.filter(email=user.email).exists():
            context['email_taken'] = True
            return render(request, 'useraccounts/register_failed.html', context)
        
        else:
            user.save()
            return render(request, 'useraccounts/register_success.html')
        

def edit_user(request):
    context = {}
    if request.method == 'POST':
        user = request.user
        
        user.email = request.POST.get('email')
        user.first_name = request.POST.get('firstname')
        user.last_name = request.POST.get('lastname')
        user.save()
        context['update_done'] = True
    return render(request, 'useraccounts/edit_user.html', context)



