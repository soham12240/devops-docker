from django.views.generic import TemplateView
from django.contrib.auth.models import User
from blog_app.models import Blog, Comment
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponseRedirect


class LoginView(TemplateView):
    template_name = "login/login.html"
    def post(self, request):
        email= request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(username=email, password=password)
        if user:
            login(request, user=user)
            return HttpResponseRedirect("/home")
        else:
            context = {"error": "Invalid email/password"}
            return super().render_to_response(context=context)
            
class SignupView(TemplateView):
    template_name = "signup/signup.html"
    def post(self, request):
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        User.objects.create_user(
            username=username, 
            password=password,
            email=email
        )
        return HttpResponseRedirect('/login')


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "home/home.html"
    login_url = '/login'
    redirect_field_name = 'redirect_to'

   

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog_list'] = Blog.objects.all()
        context['show_nav'] = True
        return context




class CreateBlogView(LoginRequiredMixin, TemplateView):
    template_name: str = "blog/create_blog.html"
    login_url = '/login'
    redirect_field_name = 'redirect_to'

    def post(self, request, *args, **kwargs):
        title = request.POST.get("title")
        content = request.POST.get("content")
        user = request.user
        blog = Blog.objects.create(
            title = title, 
            content = content, 
            author = user
        )
        return HttpResponseRedirect(f"/blog/{blog.id}")

 

class CreateCommentView(LoginRequiredMixin, TemplateView):
    template_name: str = "blog/blog.html"


    def post(self, request, id, *args, **kwargs):
        message = request.POST.get("message")
        user = request.user
        blog = Blog.objects.get(id = id)

        Comment.objects.create(
            message = message, 
            user = user, 
            blog = blog
        )

        return HttpResponseRedirect(f"/blog/{blog.id}")
        


class BlogView(LoginRequiredMixin, TemplateView):
    login_url = '/login'
    redirect_field_name = 'redirect_to'
    template_name: str = "blog/blog.html"
    def get(self, request, id=None,  *args, **kwargs):
        blog = Blog.objects.get(id = id)
        comments = Comment.objects.filter(blog=blog).order_by("id").reverse()
        return super().render_to_response(context={
            'show_nav': True,
            'blog': blog,
            'comments': comments
        })


class LogoutView(LoginRequiredMixin, TemplateView):
    template_name: str = "login/login.html"
    login_url = '/login'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        logout(request)
        return super().render_to_response({})