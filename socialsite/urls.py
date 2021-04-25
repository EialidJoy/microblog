from django.urls import path
# from socialsite.views import create_post
from . import views

urlpatterns = [
	path('', views.home, name="home"),
    path('home/', views.create_post, name="post"),
	path('home/comment', views.comment, name="comment"),    
    # path('home/login/', login_function, name="login"),
    # path('home/<int:id>/',views.create_comment, name='comment')
]