from django.conf.urls import url, patterns
from django.views.generic import TemplateView
#from picker.views import GameListView


from models import Game
from . import views

urlpatterns = patterns('picker.urls',
    #url(r'^$', views.index, name='index.html'),
    url(r'^season_(?P<pk>[0-9]+)/$', views.SeasonDetailView.as_view(), name='season_detail'),
    #url(r'^season_(?P<season>[0-9]+)/grid/$', views.GridView.as_view(), name='grid'),
    url(r'^game_(?P<pk>[0-9]+)/$', views.GameDetailView.as_view(), name='game_detail'),
    url(r'^pick_submit/$', views.PickSubmitView.as_view(), name='pick_submit'),
    url(r'join_season/$', views.join_season, name='join_season'),
    url(r'season_list/$', views.SeasonListView.as_view(), name='season_list'),
)