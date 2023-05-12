from django.shortcuts import render, redirect
from .models import introbanner, noticeboard, event, lslider, faq, gallerie, word
from django.utils import timezone
# Create your views here.

def index(request):
    ibanner = introbanner.objects.all().order_by('id')
    nomon=[]
    nody=[]
    note=[]
    evmon=[]
    evdy=[]
    even=[]

    notice = noticeboard.objects.all().order_by('-id')
    for i in range (0,5):
        month = notice[i].date.month
        day = notice[i].date.day 
        notices=notice[i]
        if month==1:
            month='January'
        elif month==2:
            month='February'
        elif month==3:
            month='March'
        elif month==4:
            month='April'
        elif month==5:
            month='May'
        elif month==6:
            month='June'
        elif month==7:
            month='July'
        elif month==8:
            month='August'
        elif month==9:
            month='September'
        elif month==10:
            month='October'
        elif month==5:
            month='November'
        else:
            month='December'
    
        nomon.append(month)
        nody.append(day)
        note.append(notices)
    
    data={
        'notices': note,
        'month': nomon,
        'day': nody,

    }
    events = event.objects.all().order_by('-id')
    print(events)

    for i in range (0,5):
        month = events[i].date.month
        day = events[i].date.day 
        eventss=events[i]
        if month==1:
            month='January'
        elif month==2:
            month='February'
        elif month==3:
            month='March'
        elif month==4:
            month='April'
        elif month==5:
            month='May'
        elif month==6:
            month='June'
        elif month==7:
            month='July'
        elif month==8:
            month='August'
        elif month==9:
            month='September'
        elif month==10:
            month='October'
        elif month==5:
            month='November'
        else:
            month='December'
    
        evmon.append(month)
        evdy.append(day)
        even.append(eventss)
    
    evdata={
        'events': even,
        'month': evmon,
        'day': evdy,

    }


    faqs = faq.objects.all().order_by('-id')
    lsliders = lslider.objects.all().order_by('-id')
    gallery = gallerie.objects.all().order_by('-id')
    words = word.objects.all().order_by('-id')
    return render(request, 'index.html', {'ibanner': ibanner, 'notice': data,'faq': faqs, 'events': evdata, 'lsliders': lsliders, 'gallery': gallery, 'words':words,})



