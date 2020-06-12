from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from .views import CreatePost,PostDetail,CreateComment
urlpatterns = [
    path('',views.index,name="index"),
    path("home",views.home,name="home"),
    path("profile",views.Profile,name="profile"),
    path("logout",LogoutView.as_view(),name="logout"),
    path("login",views.Login,name="login"),
    path("create",CreatePost.as_view(),name="create"),
    path("<int:pk>/comment",views.CreateComment,name="comment"),
    path("post-detail/<int:pk>",PostDetail.as_view(),name="post-detail"),


]
