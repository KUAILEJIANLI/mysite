from django.urls import path
from . import views
from django.contrib.staticfiles.urls import static
import mysite.settings as settings

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('index/', views.index),
    path('login/', views.login),
    path('register/', views.register),
    path('logout/', views.logout),
]