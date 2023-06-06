from MyForm import views
from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
]

urlpatterns += staticfiles_urlpatterns()