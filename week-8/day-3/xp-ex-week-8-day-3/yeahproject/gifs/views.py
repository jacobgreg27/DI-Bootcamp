from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.db.models import F



from .models import Gif, Category
from .forms import GifForm, CategoryForm

# Create your views here.
# Create some views:
# Homepage view: this view will display all the gifs from the database. Display each gif in an img tag.
# Add a navbar, with links that redirect the user to the Add new GIF view and to the Add new Category view.

# Add new GIF view: this view will use the GifForm created above, to add a new gif to the database.

# Add new Category view: this view will use the CategoryForm created above, to add a new category to the database.

# Category view: this view accepts a category id as a parameter and displays all gifs with that category (ie. for example all the “happy” gifs).

# Categories view: this view will display all the existing categories from the database. Each category has a link redirecting the user to the Category view.

# Gif view: this views accepts a gif id and display that specific gifs details on the page. Display each gif in an img tag.

# Create routes and templates in accordance to the views.
def popular_gifs(request):
    gifs = Gif.objects.annotate(like_diff=F('likes')-1).filter(like_diff__gt=0).order_by('-likes')
    return render(request, 'gifs/popular_gifs.html', {'gifs': gifs})

def homepage(request):
    gifs = Gif.objects.all()
    return render(request, 'gifs/homepage.html', {'gifs': gifs})

class GifCreateView(CreateView):
    model = Gif
    form_class = GifForm
    template_name = 'gifs/gif_form.html'

    def form_valid(self, form):
        form.instance.uploader_name = self.request.user.username
        return super().form_valid(form)
    
def category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    gifs = category.gifs.all()
    return render(request, 'gifs/category.html', {'gifs': gifs, 'category': category})

def categories(request):
    categories = Category.objects.all()
    return render(request, 'gifs/categories.html', {'categories': categories})

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'gifs/category_form.html'

def gif(request, gif_id):
    gif = get_object_or_404(Gif, id=gif_id)
    return render(request, 'gifs/gif.html', {'gif': gif})