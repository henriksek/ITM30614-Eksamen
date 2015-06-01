from django.shortcuts import render

from message_app.models import Message

# Create your views here.

def frontpage(request):
    messages = Message.objects.all()
    context = {'messages': messages}
    return render(request, 'theme/frontpage.html', context)