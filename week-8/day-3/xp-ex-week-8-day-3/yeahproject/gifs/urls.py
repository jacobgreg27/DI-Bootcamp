from django.urls import path
from .views import homepage, GifCreateView, category, categories, CategoryCreateView, gif
from . import views


app_name = 'gifs'

urlpatterns = [
    path('', homepage, name='homepage'),
    path('gif/add/', GifCreateView.as_view(), name='add_gif'),
    path('category/<int:category_id>/', category, name='category'),
    path('categories/', categories, name='categories'),
    path('category/add/', CategoryCreateView.as_view(), name='add_category'),
    path('gif/<int:gif_id>/', gif, name='gif'),
    path('popular-gifs/', views.popular_gifs, name='popular_gifs'),
]
