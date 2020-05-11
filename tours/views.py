from django.db.models import Sum
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from locations.models import Location


@csrf_exempt
def get_minimum_and_type(request):
    location_ids = request.POST.getlist('location_ids[]')
    total_minutes = Location.objects.filter(id__in=location_ids).aggregate(Sum('min_time'))
    tour_type = "Long tour" if total_minutes.get('min_time__sum') > 40 else "Short tour"
    return JsonResponse({'total_minutes': total_minutes.get('min_time__sum'), "tour_type": tour_type})
