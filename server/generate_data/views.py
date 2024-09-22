from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
import sys

sys.path.append('/Users/tanpham/Documents/personal_project/customer-data-platform/generators')

import main_generators

# Create your views here.
def generate_customers(request):
    data = main_generators.generate_more_customers()
    return JsonResponse(data, safe=False)

def generate_products(request):
    data = main_generators.generate_more_products()
    return JsonResponse(data, safe=False)

def generate_orders(request):
    data = main_generators.generate_more_orders()
    return JsonResponse(data, safe=False)

def main(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render(request=request))