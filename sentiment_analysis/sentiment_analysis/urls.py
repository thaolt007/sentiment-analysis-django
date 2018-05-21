from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sentiment_analysis.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^lazada/', include('lazada.urls', namespace='lazada')),
    url(r'^admin/', include(admin.site.urls)),
)
