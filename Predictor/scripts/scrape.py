import urllib3
#from bs4 import BeautifulSoup
from Predictor.models import Passenger
from subprocess import call

def scrape():
    test_data = Passenger.objects.all().filter(passenger_type='test')
    if !test_data:
       call('python3 manage.py import')
    test_data = Passenger.objects.all.filter(passenger_type='test')
    http = urllib3.PoolManager()
    for passenger in test_data:
        name = passenger.url_name()
        req = http.request('GET', 'https://www.encyclopedia-titanica.org/titanic-survivor/' + name + '.html')
        if req.status == 200:
            passenger.survived = 1
            passenger.save()
            print("passenger ${name} survived".format(name=passenger.passenger_name)
        else:
            passenger.survived = 0
            passenger.save()
            print("passenger ${name} died")
        usleep(500)

        #body = BeautifulSoup(req.data, 'html.parser')
        
