from django.shortcuts import render

# Create your views here.
import json

def family_view(request, pk):
    with open('./animals.json') as f:
        data = json.load(f)

    family = None
    for f in data['families']:
        if f['id'] == pk:
            family = f
            break

    animals = []
    for a in data['animals']:
        if a['family'] == pk:
            animals.append(a)
    print(family)
    context = {
        'family': family,
        'animals': animals,
    }
    return render(request, 'info/family.html', context)

def animal_view(request, pk):
    with open('animals.json') as f:
        data = json.load(f)

    animal = None
    for a in data['animals']:
        if a['id'] == pk:
            animal = a
            break
    print(animal)
    context = {
        'animal': animal,
    }
    return render(request, 'info/animal.html', context)
