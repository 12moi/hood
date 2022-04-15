from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.signup, name='signup'),
    path('account/', include('django.contrib.auth.urls')),
    path('all-hoods/', views.hoods, name='hood'),
    path('new-hood/', views.create_hood, name='new-hood'),
    path('new-hood/', views.create_hood, name='new-hood'),
    path('profile/<username>', views.profile, name='profile'),
    path('profile/<username>/edit/', views.edit_profile, name='edit-profile'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)