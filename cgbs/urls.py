from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.views.generic import TemplateView, CreateView
from registration.forms import UserCreationForm
from picker.views import SeasonListView

from registration.backends.default.views import ActivationView, RegistrationView



urlpatterns = patterns('',

    url(r'^issues/', 
        TemplateView.as_view(template_name='issues.html'),
        name='issues'),

    url(r'^admin/', include(admin.site.urls)),
    
    (r'^picker/', include('picker.urls', namespace='picker', app_name='picker')),
    
    url(r'^accounts/activate/complete/$',
        TemplateView.as_view(template_name='registration/activation_complete.html'),
        name='registration_activation_complete'),
    # Activation keys get matched by \w+ instead of the more specific
    # [a-fA-F0-9]{40} because a bad activation key should still get to the view;
    # that way it can return a sensible "invalid key" message instead of a
    # confusing 404.
    url(r'^accounts/activate/(?P<activation_key>\w+)/$',
       ActivationView.as_view(),
       name='registration_activate'),
    url(r'^accounts/register/$',
       RegistrationView.as_view(),
       name='registration_register'),
    url(r'^accounts/register/complete/$',
       TemplateView.as_view(template_name='registration/registration_complete.html'),
       name='registration_complete'),
    url(r'^accounts/register/closed/$',
       TemplateView.as_view(template_name='registration/registration_closed.html'),
       name='registration_disallowed'),
    (r'', include('registration.auth_urls')),

    
    url(r'^$', SeasonListView.as_view(), name='index'),

    
    # When you make your registration forms...
    # http://stackoverflow.com/questions/6414926/how-to-use-different-form-in-django-registration
)