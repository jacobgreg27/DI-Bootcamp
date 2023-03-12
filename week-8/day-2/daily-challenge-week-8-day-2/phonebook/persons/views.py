from django.shortcuts import render, get_object_or_404
from .models import Person

def search_by_phone_number(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        try:
            person = Person.objects.get(phone_number=phone_number)
            return render(request, 'persons/person_detail.html', {'person': person})
        except Person.DoesNotExist:
            return render(request, 'persons/person_not_found.html')
    return render(request, 'persons/search_by_phone_number.html')

def search_by_name(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        try:
            person = Person.objects.get(name=name)
            return render(request, 'persons/person_detail.html', {'person': person})
        except Person.DoesNotExist:
            return render(request, 'persons/person_not_found.html')
    return render(request, 'persons/search_by_name.html')

