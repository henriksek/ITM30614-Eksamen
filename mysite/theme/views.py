from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from message_app.models import Message

# Create your views here.

def frontpage(request):
    messages = Message.objects.all().order_by('-created_datetime')
    
    page_nr = request.GET.get('page')
    paginator = Paginator(messages, 10)
    
    try:
        messages = paginator.page(page_nr)
    
    except PageNotAnInteger:
        # If the page is not an integer, go to first page
        messages = paginator.page(1)
    
    except EmptyPage:
        # If the page is bigger then the number of pages, go to the last page with items on it
        messages = paginator.page(paginator.num_pages)
    
    context = {
        'messages': messages,
        'paginator': paginator,
    }
    return render(request, 'theme/frontpage.html', context)