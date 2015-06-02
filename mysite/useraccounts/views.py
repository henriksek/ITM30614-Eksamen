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
            context['login_failed'] = True
            return render(request, 'theme/frontpage.html', context)

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
        
        elif User.objects.filter(email=user.email).exists():
            context['email_taken'] = True
        
        else:
            user.save()
            context['register_successfull'] = True
        
        return render(request, 'theme/frontpage.html', context)

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



