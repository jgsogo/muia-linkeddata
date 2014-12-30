from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import Home, About, Ontology, OntologyRedirect

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'linkeddata.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', Home.as_view(), name='home'),
    url(r'^about/$', About.as_view(), name='about'),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^linkeddata/def/rafco$', OntologyRedirect.as_view(), name='ontology-redirect'),
    url(r'^ontology/$', Ontology.as_view(), name='ontology'),
)
