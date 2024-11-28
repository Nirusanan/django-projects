from django.shortcuts import render, redirect
from .models import Song
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    all_songs = Song.objects.all()
    paginator = Paginator(all_songs, 1)
    page_number = request.GET.get('page')
    page_obj =  paginator.get_page(page_number)

    return render(request, 'index.html', {'page_obj': page_obj})
