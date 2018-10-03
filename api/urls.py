from django.conf.urls import url, include
from django.contrib import admin

admin_root_url = r'^services/admin/'

urlpatterns = [
    url(admin_root_url, admin.site.urls),
    url(r'^services/api/', include('accounts.urls')),
]
