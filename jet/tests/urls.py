from django.conf.urls import include, url
from django.contrib import admin

admin.autodiscover()

from django.urls import path

urlpatterns = [
        url(r'^jet/', include('jet.urls', 'jet')),
        url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
        url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
        path('admin/', admin.site.urls),
]

