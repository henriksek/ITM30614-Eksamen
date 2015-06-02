from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from message_app.models import Message

# Create your views here.

def new_message(request):
    if request.method == 'POST':
        message = Message()
        message.content = request.POST.get('content')
        message.created_by = request.user
        message.created_datetime = timezone.now()
        message.save()
    
    return redirect('frontpage')

def message_detail(request, message_id):
    message = Message.objects.get(pk=message_id)
    
    #user for facebook open graph
    current_url = request.get_full_path()
    
    context = {
        'message': message,
        'current_url': current_url
    }
    
    return render(request, 'message_app/message_detail.html', context)

@login_required
def like_message(request, message_id):
    if request.is_ajax():
        message = Message.objects.get(pk=message_id)
        user = request.user
        
        try:
            user_liked = user.likes.get(pk=message_id)
        except:
            user_liked = False
        
        #If user has allready liked this message, unlike
        if user_liked:
            message.likes.remove(user)
            message.total_likes -= 1
            message.save()
            liked = False
        
        #If user hasnt liked, like
        else:
            message.likes.add(user)
            message.total_likes += 1
            message.save()
            liked = True
        
        data = {
            'total_likes': message.total_likes,
            'liked': liked
        }
        return JsonResponse(data)