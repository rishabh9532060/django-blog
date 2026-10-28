from django.urls import path
from . import views
urlpatterns = [
    path('',views.postlists,name='postlist'),
    path('post_detail/<id>/',views.post_detail,name='post_detail'),

]
