import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','covid_proj.settings')

import django

django.setup()




from newsapi import NewsApiClient
import datetime

def run():
    newsapi = NewsApiClient(api_key='c1344e4bd8e1478a9c536aba22791d5b')

    tod = datetime.datetime.now()
    d = datetime.timedelta(days = 7)
    a = str(tod - d)

    todays = str(tod).split(" ")[0]
    past = a.split(" ")[0]

    # /v2/top-headlines
    news = newsapi.get_everything(q='coronavirus, covid19, covid-19, corona',
                                      from_param=past,
                                      to=todays,
                                      language='en')
    for i in range(0, len(news['articles'])):
        print(news['articles'][i]['title'])

if __name__ == '__main__':
    run()
