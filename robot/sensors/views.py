import json
from django.http import HttpResponse
from django.core.serializers import serialize
from .models import Reflectance
from .models import Distance

def reflectance(request):
    qs = Reflectance.objects.order_by("-timeStamp")
    qs = qs[len(qs)-1:]
    data = serialize("json", qs)
    print(data)
    return HttpResponse(data)

def distance(request):
    qs = Distance.objects.order_by("-timeStamp")
    qs = qs[len(qs)-1:]
    data = serialize("json", qs)
    print(data)
    return HttpResponse(data)