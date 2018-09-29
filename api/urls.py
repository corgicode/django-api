from django.conf.urls import url, include
from django.contrib import admin
# from adminplus.sites import AdminSitePlus

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]

# admin.site = AdminSitePlus()
# admin.sites.site = admin.site
# admin.autodiscover()

admin.site.site_header = 'codecorgi Admin'

admin_root_url = r'^services/admin/'

urlpatterns = [
    url(admin_root_url, include(admin.site.urls)),
    # url(r'^services/api/', include('usermanagement.urls')),
    # url(r'^services/api/', include('challenges.urls')),
]
