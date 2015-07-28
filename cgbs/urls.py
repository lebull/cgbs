from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.views.generic import TemplateView
from picker.views import SeasonListView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cgbs.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    
    (r'^picker/', include('picker.urls', namespace='picker', app_name='picker')),
    
    url(r'^$', SeasonListView.as_view(), name='index'),
    
    # When you make your registration forms...
    # http://stackoverflow.com/questions/6414926/how-to-use-different-form-in-django-registration
)