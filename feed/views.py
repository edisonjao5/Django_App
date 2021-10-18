from django.contrib import messages 
from django.db import models
from django.views.generic import TemplateView, DetailView, FormView
from .models import Post
from .forms import PostForm, ContactForm

class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all().order_by("id")
        return context

class LoginView(FormView):
    template_name = "login.html"
    form_class = ContactForm
    success_url = "/login/"

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)

class PostDetailView(DetailView):
    template_name = "detail.html"
    model = Post

class AddPostView(FormView):
    template_name = "new_post.html"
    form_class = PostForm
    success_url = "/"

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        new_object = Post.objects.create(
            text = form.cleaned_data['text'],
            image = form.cleaned_data['image']
        )
        messages.add_message(self.request, messages.SUCCESS, 'The Post has been loaded correctly')
        return super().form_valid(form)