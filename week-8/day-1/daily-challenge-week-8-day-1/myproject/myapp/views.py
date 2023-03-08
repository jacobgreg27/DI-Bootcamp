from django.shortcuts import render

# Create your views here.
# from django.shortcuts import render
from .models import Person

def people(request):
    people = Person.objects.all().order_by('age')
    return render(request, 'people.html', {'people': people})

def person(request, id):
    person = Person.objects.get(id=id)
    return render(request, 'person.html', {'person': person})
