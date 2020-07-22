from django.conf.urls import url

urlpatterns = [
    url(r'^$', UserController.as_view()),
    url(r'^section/$', UserController.as_view()),
    url(r'^question/$', UserController.as_view()),
    url(r'^answer/$', UserController.as_view()),
]