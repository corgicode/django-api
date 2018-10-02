from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]

admin.autodiscover()

admin.site.site_header = 'codecorgi Admin'

admin_root_url = r'^services/admin/'

urlpatterns = [
    url(admin_root_url, include(admin.site.urls)),
    # url(r'^services/api/', include('usermanagement.urls')),
    # url(r'^services/api/', include('challenges.urls')),
]
