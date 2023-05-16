from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Person, Action
from django.db.models import Avg

def person_info(request, person_id):
    person = get_object_or_404(Person, id=person_id)
    actions = Action.objects.filter(person=person)
    positive_actions = actions.filter(rating__gt=5).count()
    neutral_actions = actions.filter(rating=5).count()
    negative_actions = actions.filter(rating__lt=5).count()
    average_rating = actions.aggregate(Avg('rating'))['rating__avg']
    data = {
        'name': person.first_name + ' ' + person.last_name,
        'positive_actions': positive_actions,
        'neutral_actions': neutral_actions,
        'negative_actions': negative_actions,
        'average_rating': average_rating
    }
    return JsonResponse(data)

def married_unemployed_in_city_n(request):
    count = Person.objects.filter(
           is_married=True, 
           is_unemployed=None, 
           addresses__city='N').annotate(
           avg_rating=Avg('actions__rating')).filter(avg_rating__gt=6).count()
    return JsonResponse({'count': count})