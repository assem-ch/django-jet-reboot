from django.conf.urls import include
from django.contrib import admin

admin.autodiscover()

from django.urls import path

urlpatterns = [
        path(r'jet/', include('jet.urls', 'jet')),
        path(r'jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
        path(r'admin/doc/', include('django.contrib.admindocs.urls')),
        path('admin/', admin.site.urls),
]

