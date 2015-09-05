from django.conf.urls import url, patterns
from django.views.generic import TemplateView
#from picker.views import GameListView


from models import NewsPost
from . import views

urlpatterns = patterns('news.urls',
    url(r'^(?P<pk>[-\w]+)/$', views.NewsPostDetailView.as_view(), name='newspost_detail'),
    url(r'^$', views.NewsPostListView.as_view(), name='newspost_list'),
    #url(r'^$', views.NewsPostDetailView.as_view(), name='news_list'),
)