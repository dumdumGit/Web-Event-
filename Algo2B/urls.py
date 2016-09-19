from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Algo2B.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^$','dp_event.views.index'),
    (r'^', include('dp_event.urls')),
    (r'^admin/', include(admin.site.urls)),




) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
