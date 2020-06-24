from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.FeedList.as_view(), name="feed_list"),
    path('<int:feed_pk>/', views.FeedDetail.as_view(), name="feed_detail"),
    path('<int:feed_pk>/comments/', views.FeedCommentList.as_view(), name="feed_comment_list"),
    path('<int:feed_pk>/comments/<int:comment_pk>/', views.FeedCommentDetail.as_view(), name="feed_comment_detail"),
]