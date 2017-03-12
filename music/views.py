from django.shortcuts import render

# Create your views here.
from .models import Album
from django.shortcuts import render
from django.http import Http404


def index(request):
    all_albums = Album.objects.all()
    return render(request, 'music/index.html', {'all_albums': all_albums})


def detail(request, albun_id):
    try:
        album = Album.objects.get(pk=albun_id)
    except Album.DoesNotExist:  #id不存在异常
        raise Http404("Album dies now exist")
    return render(request, 'music/detail.html', {'album': album})
