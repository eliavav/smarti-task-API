from django.urls import re_path
from UserApp import views


urlpatterns = [
    re_path(r'^user$', views.usersAPI),
    re_path(r'^user/([0-9]+)$', views.usersAPI),
    re_path(r'^user/search$', views.search)
]
