from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, AccessRecord, Webpage
# Create your views here.

#def index(request):
#    my_dict = {'insert_me':'Hello, I am from views.py'}
#    return render(request, 'first_app/index.html', context=my_dict)

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    my_dict = {'access_records':webpages_list}
    return render(request, 'first_app/index.html', context=my_dict)
