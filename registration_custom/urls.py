from django.conf.urls import url, patterns, include
#from picker.views import GameListView



urlpatterns = patterns('',

        url(r'^password_change/$', 
            'django.contrib.auth.views.password_change', 
            name='password_change'),
        url(r'^$', include('registration.backends.default.urls')),
    
)