import json

from django.views.decorators.csrf import csrf_exempt

from .models import Order, Person
from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.

@csrf_exempt
def create_order(request):
    if request.method == "POST":
        data = json.loads(request.body)
        name = data.get("name")
        city = data.get("city")
        offer = data.get("offer")
        price = data.get("price")
        order = Order.objects.create(name=name, city=city, offer=offer, price=price)
        order.save()
        return JsonResponse({"message": "Order created successfully"})

#create_query
@csrf_exempt
def create_person(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get("name")
        address = data.get("address")
        person = Person.objects.create(name=name, address=address)
        person.save()
        return JsonResponse({"message": "Person created"})

#read_all_query
@csrf_exempt
def read_orders(request):
    order = Order.objects.all().values()
    return JsonResponse({"data": list(order)})

#read_one_query
@csrf_exempt
def read_order(request):
    data = json.loads(request.body)
    id = data.get("id")
    order = Order.objects.get(id=id)
    response_dict = {
        "name": order.name,
        "price": order.price,
        "city": order.city
    }
    return JsonResponse(response_dict)

#filter_query
@csrf_exempt
def fetch_by_city(request):
    if request.method == "POST":
        data = json.loads(request.body)
        city = data.get("city")
        order = Order.objects.filter(city=city).values()
        response = {
            "data": list(order)
        }
        return JsonResponse(response)

#update_query
@csrf_exempt
def person_update(request):
    data = json.loads(request.body)
    person = Person.objects.get(name=data.get("name"))
    person.address = data.get("address")
    person.save()
    return JsonResponse({"data": "updated successfully"})

#delete_query
@csrf_exempt
def person_delete(request):
    data = json.loads(request.body)
    person = Person.objects.get(name=data.get("name"))
    person.delete()
    return JsonResponse({"data": "deleted successfully"})

