from django.urls import path

from . import views

user_list = views.UserViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

urlpatterns = [
    path('', user_list)
]
