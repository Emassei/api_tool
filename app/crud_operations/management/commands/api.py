from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from datetime import datetime
from django.http import HttpResponse
import requests
import json
import time
import logging
import re
import os
import csv


url = 'http://jsonplaceholder.typicode.com/users'



def write_csv(name,email,street,zipcode):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="test_users.csv"'

    writer = csv.writer(response)
    writer.writerow([name,email,street,zipcode])

    return response

def data_pull(url):
    response = requests.get(url)
    json_list = response.json()
    __import__('pudb').set_trace()
    for item in json_list:
        name = item['name']
        email = item['email']
        street = item['address']['street'] + item['address']['suite']
        zip_code = item['address']['zipcode']
        write_csv(name,email,street,zip_code)
    print('done')

class Command(BaseCommand):
    def handle(self, *args, **options):
        data_pull(url)


