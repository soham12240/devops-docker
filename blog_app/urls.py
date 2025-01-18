from django.urls import path 
from .views import *


urlpatterns = [
    path("", LoginView.as_view(), name="root_view"),
    path("login", LoginView.as_view(), name="login_view"),
    path("signup", SignupView.as_view(), name="signup_view"),
    path("home", HomeView.as_view(), name="home_view"),
    path("create_blog_view", CreateBlogView.as_view(), name="create_blog_view"),
    path("blog/<int:id>", BlogView.as_view(), name="blog_view"),
    path("logout", LogoutView.as_view(), name="logout"),
    path("comment_on_blog/<int:id>", CreateCommentView.as_view(), name="comment_on_blog")
]