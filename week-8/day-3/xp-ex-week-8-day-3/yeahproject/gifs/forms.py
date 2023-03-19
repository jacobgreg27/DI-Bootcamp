# Part II - Forms And Views
# Create a forms.py,file and add two new forms:
# GifForm with the fields
# uploader_name
# title
# url : You can use the gifs’ url from the giphy website. Click on the gif you want, and copy the gif link.
# categories : look up ModelMultipleChoiceField

# CategoryForm with the fields
# name



from django import forms

from gifs.models import Gif, Category

class GifForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )


    class Meta:
        model = Gif
        fields = ('title', 'url', 'uploader_name', 'categories')

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)        