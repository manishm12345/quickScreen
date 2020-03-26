from django.urls import path, include, re_path
from . import views

urlpatterns = [
    # PAGES
    path('', views.start_test, name='start'),
    path("test_instructions/", views.test_instructions, name='test_instructions'),
    path("hello_template/", views.hello_template, name='helloTemplate'),
    # catchall path for receiving the hash of the user
    re_path(r"x/.*", views.evaluate_hash),
]