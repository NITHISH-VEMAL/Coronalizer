import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','covid_proj.settings')

import django

django.setup()

from covid_app.models import MyModel
import COVID19Py
covid19 = COVID19Py.COVID19()

def run():
    location = covid19.getLocationByCountryCode("IN", timelines=True)
    timeline = location[0]["timelines"]["confirmed"]["timeline"]
    #a = Album.objects.get(pk = 3)
    #a.genre = "Pop"
    #a.save()
    timing_str = ""
    cases_int = 0

    for key in timeline.keys():
        print(key, '->', timeline[key])
        count_if = MyModel.objects.filter(timing = key).count()
        if(count_if > 0):

            b = MyModel.objects.get(timing = key)
            b.cases = timeline[key]

            b.save()
        else:

            b = MyModel(timing=key, cases=timeline[key])
            b.save()


#print(location)
if __name__ == '__main__':
    run()
