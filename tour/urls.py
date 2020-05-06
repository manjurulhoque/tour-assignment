from django.contrib import admin
from django.urls import path

admin.site.site_header = "Tour Admin"
admin.site.site_title = "Site Admin"
admin.site.index_title = 'Features List'

urlpatterns = [
    path('admin/', admin.site.urls),
]
