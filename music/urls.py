
# 导入当前目录下的views
from .import views
from django.conf.urls import url

app_name='music'


urlpatterns = [
    # /music/
    url(r'^$',views.IndexView.as_view(),name='index'),

#     /music/album_id/
    url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(),name='detail'),

#     /music/album_id/favorite/
    url(r'^(?P<album_id>[0-9]+)/favorite/$',views.favorite,name='favorite'),

    url(r'album/add/$',views.AlbumCreate.as_view(),name='album-add')
]













