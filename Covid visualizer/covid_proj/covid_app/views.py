from django.shortcuts import render, redirect
from django.views.generic import (ListView, TemplateView)
from .models import MyModel,Suggest
from django.shortcuts import render
from django.http import HttpResponse
import matplotlib.pyplot as plt
import io
#from fusioncharts import FusionCharts
import urllib, base64
#from ..models import *
import datetime
from covid import Covid

from django.shortcuts import render
from newsapi import NewsApiClient

# Create your views here.



def news(request):

    newsapi = NewsApiClient(api_key ='c1344e4bd8e1478a9c536aba22791d5b')

    top = newsapi.get_everything(q='covid19',
                                      sort_by='publishedAt',
                                      #sources='',
                                      language='en')

    l = top['articles']
    desc =[]
    news =[]
    publish =[]
    link =[]

    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        publish.append(f['publishedAt'])
        link.append(f['url'])
    mylist = zip(news, desc, publish, link)



    return render(request, 'covid_app/MyNews_list.html', context ={"mylist":mylist})


class MyModelListView(ListView):
    model = MyModel
    template_name = 'covid_app/MyModel_list.html'

    def get_queryset(self):

        cases = []
        queryset = MyModel.objects.all()
        for post in queryset:
            cases.append(post.cases)

    #    render('covid_app/MyModel_list.html', {'cases': cases,})


        tod = datetime.datetime.now()
        d = datetime.timedelta(days = 8)
        a = str(tod - d)



        return MyModel.objects.filter(timing__gte=a.split()[0]+'T00:00:00Z')


    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        covid = Covid(source="worldometers")
        covid.get_data()

        india_cases = covid.get_status_by_country_name("india")
        data['india_cases'] = india_cases
        return data

def index(request):
    return render(request, 'covid_app/base.html', context ={})

def about(request):
    if request.method == 'POST':
        s = Suggest(suggestions=request.POST.get('suggest'))
        s.save()
        return render(request, 'covid_app/about.html', context ={'s':s})

    else:

        return render(request, 'covid_app/about.html', context ={})
