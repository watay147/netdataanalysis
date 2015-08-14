#encoding=utf8
from django.shortcuts import render
from django.http import HttpResponse
from .models import company
from .models import events
from .models import news
from .models import statics
from django.shortcuts import get_object_or_404
from django.db.models import Q
import json

# Create your views here.

def index(request):
    topcredit_list=company.objects.order_by('creditorder').all()[:10]
    attention_list=company.objects.filter(attention=True)[:10]
    topnew_list=news.objects.order_by('-hot').all()[:10]
    topevent_list=events.objects.order_by('-hot').all()[:10]
    context = {'topcredit_list': topcredit_list,
                'attention_list':attention_list,
                'topnew_list':topnew_list,
                'topevent_list':topevent_list}
    return render(request,'index.html', context)

def indexcreditorders(request):
    order_list=company.objects.order_by('creditorder').all()
    monorder_list=company.objects.order_by('moncreditorder').all()
    weekorder_list=company.objects.order_by('weekcreditorder').all()
    context = {'order_list': order_list,'monorder_list':monorder_list,'weekorder_list':weekorder_list}
    return render(request,'indexcreditorders.html',context)

def indexevents(request):
    event_list=events.objects.order_by('hot').all()
    context = {'event_list': event_list}
    return render(request,'indexevents.html',context)

def indexnews(request):
    new_list=news.objects.order_by('hot').all()
    context = {'new_list': new_list}
    return render(request,'indexnews.html',context)

def indexattentions(request):
    attention_list=company.objects.filter(attention=True)
    return render(request,'indexattentions.html',{'attention_list':attention_list})

def indexsearch(request):
    company_list=company.objects.filter(Q(name__icontains=request.GET['item'])|Q(stockno__icontains=request.GET['item']))
    context={'company_list':company_list}
    return render(request,'indexsearch.html',context)

def viewcompany(request,stockno):
    acompany=get_object_or_404(company, stockno=stockno)
    event_list=events.objects.order_by('hot').filter(stockno=stockno)
    new_list=news.objects.order_by('hot').filter(stockno=stockno)
    context={"company":acompany,
            "event_list":event_list,
            "new_list":new_list}
    return render(request,'company.html',context)

def comintro(request,stockno):
    acompany=get_object_or_404(company, stockno=stockno)
    context={"company":acompany}
    return render(request,'comintro.html',context)

def comfinance(request,stockno):
    acompany=get_object_or_404(company, stockno=stockno)
    context={"company":acompany}
    return render(request,'comfinance.html',context)

def eventstipslist(request):
    stockno=request.GET['stockno']
    xAxis=request.GET['xAxis']
    eventdata=events.objects.order_by('-hot').filter(Q(stockno=stockno)&Q(date=xAxis))
    if request.GET['count']!='full':
        eventdata=eventdata[:int(request.GET['count'])]
    result=[{'title':x.title,'id':x.id,'click':x.click,'reply':x.reply,'source':x.source} for x in eventdata]
    return HttpResponse(json.dumps(result), content_type="application/json")

def linedata(stockno,sta,end):
    plotdata=statics.objects.order_by('stadate').filter(Q(stockno=stockno)&Q(stadate__gte=sta)&Q(stadate__lte=end))
    result={}
    result['legend']=[u'舆情指数',u'股价']
    result['category']=[str(x.stadate) for x in plotdata]#只能使用.xx访问而不是['xx']
    result['series']=[]
    result['series'].append({
        'name':u'舆情指数',
        'type':'line',
        'data':[x.creditindex for x in plotdata],
        'markPoint':{
            'data':[{'xAxis':str(x.stadate),'yAxis':x.creditindex} for x in plotdata if x.shouldmark]
        }
        })
    result['series'].append({
        'name':u'股价',
        'type':'line',
        'yAxisIndex':1,
        'data':[x.price for x in plotdata]
        })
    return HttpResponse(json.dumps(result), content_type="application/json")

def piedata(stockno,sta,end):
    piedata=statics.objects.filter(Q(stockno=stockno)&Q(stadate__gte=sta)&Q(stadate__lte=end))
    possent=sum([x.possent for x in piedata])
    negsent=sum([x.negsent for x in piedata])
    neusent=sum([x.neusent for x in piedata])
    total=possent+negsent+neusent
    result={}
    result['legend']=[u'正向',u'负向',u'中性']
    result['series']=[]
    result['series'].append({
        'name':u'占比',
        
        'type':'pie',
        'center': ['30%', '60%'],
        'data':[
        {'value':float(possent)/total,'name':u'正向'},
        {'value':float(negsent)/total,'name':u'负向'},
        {'value':float(neusent)/total,'name':u'中性'}
        ]
        })
    return HttpResponse(json.dumps(result), content_type="application/json")

def complotdata(request):
    stockno=request.GET['stockno']
    plottype=request.GET['type']
    if plottype=='line':
        return linedata(stockno,request.GET['sta'],request.GET['end'])
    elif plottype=='pie':
        return piedata(stockno,request.GET['sta'],request.GET['end'])


def viewevent(request,eventsid):
    article=events.objects.get(id=eventsid)
    context={"article":article}
    return render(request,'article.html',context)

def viewnew(request,newsid):
    article=news.objects.get(id=newsid)
    context={"article":article}
    return render(request,'article.html',context)




