
# 导入当前目录下的views
from . import  views
from django.conf.urls import url


urlpatterns = [
    # /music/
    url(r'^$',views.index,name='index'),

#     /music/id/
    url(r'^(?P<albun_id>[0-9]+)/$',views.detail,name='detail'),

]