
# 导入当前目录下的views
from . import  views
from django.conf.urls import url

app_name='music'


urlpatterns = [
    # /music/
    url(r'^$',views.index,name='index'),

#     /music/album_id/
    url(r'^(?P<album_id>[0-9]+)/$',views.detail,name='detail'),

#     /music/album_id/favorite/
    url(r'^(?P<album_id>[0-9]+)/favorite/$',views.favorite,name='favorite'),
]













