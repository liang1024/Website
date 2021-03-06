
# Create your views here.
from django.shortcuts import get_object_or_404, render

from .models import Album,Song
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView


class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = "all_albums"
    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'


class AlbumCreate(CreateView):
    model = Album
    fields = ['artist','album_title','genre','album_logo']
    template_name = 'music/album_from.html'



def favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song=album.song_set.get(pk=request.POST['song'])
    except(KeyError,Song.DoesNotExist):
        return render(request,'music/detail.html',
                      {'album':album,
                    'error_message':'You did not select a valid song'})
    else:
        selected_song.is_favorite=True
        selected_song.save()
        return render(request, 'music/detail.html', {'album': album})















