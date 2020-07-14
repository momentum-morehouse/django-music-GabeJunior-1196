from django.shortcuts import render
from .models import Album, Users

# Create your view here,
def index(request):
  return render(request, 'albums/list_albums.html', context={'albums':albums})