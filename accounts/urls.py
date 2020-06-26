from django.urls import path
from . import views
app_name = 'accounts'

urlpatterns = [
    path('<username>/', views.UserDetail.as_view()),
    path('<username>/follow/', views.Follow.as_view()),
    path('<username>/unfollow/', views.UnFollow.as_view()),
    path('<username>/followings/', views.UserFollowings.as_view()),
    path('<username>/followers/', views.UserFollowers.as_view()),
]