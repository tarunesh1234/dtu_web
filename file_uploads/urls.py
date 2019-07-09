from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from .views import notes 

urlpatterns = [
	path('',notes, name='notes'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)