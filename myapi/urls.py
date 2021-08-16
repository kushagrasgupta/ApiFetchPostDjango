from django.contrib import admin
from django.urls import path
from myapi import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.static import serve


urlpatterns = [
    path('admin/', admin.site.urls),
    path('userinfo/', views.ImageViewSet.as_view()),
    url('media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,})
]

