from django.urls import path
# from socialsite.views import create_post
from . import views

urlpatterns = [
    path('login/', views.login, name="login"),
    # path('home/login/', login_function, name="login"),
    path('register/',views.register, name='register'),
    path('logout/',views.logout, name='logout')
]