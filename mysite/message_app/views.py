from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import redirect

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
    
    context = {'message': message}
    
    return render(request, 'message_app/message_detail.html', context)
    