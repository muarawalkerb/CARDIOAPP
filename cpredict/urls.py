from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name="home-page"),
    path('predict', views.predict, name="predict-page"),
    path('comment', views.comment, name="contact-page"),
]