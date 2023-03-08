from django.shortcuts import render


# Define the list of dictionaries
PEOPLE = [
  {
    'id': 1,
    'name': 'Bob Smith',
    'age': 35,
    'country': 'USA'
  },
  {
    'id': 2,
    'name': 'Martha Smith',
    'age': 60,
    'country': 'USA'
  },
  {
    'id': 3,
    'name': 'Fabio Alberto',
    'age': 18,
    'country': 'Italy'
  },
  {
    'id': 4,
    'name': 'Dietrich Stein',
    'age': 85,
    'country': 'Germany'
  }
]

# Define your view functions here
def people_list(request):
    people = sorted(PEOPLE, key=lambda x: x['age'])
    context = {'people': people}
    return render(request, 'people_list.html', context)


def person_detail(request, id):
    person = next((p for p in PEOPLE if p['id'] == int(id)), None)
    context = {'person': person}
    return render(request, 'person_detail.html', context)