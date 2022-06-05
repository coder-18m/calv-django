from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Post, Category
from .forms import PostForm
from django.urls import reverse_lazy


# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class DevelopmentView(TemplateView):
    template_name = 'development_sum.html'

class DevelopmentMapView(TemplateView):
    template_name = 'develop_map.html'

class TransportMapView(TemplateView):
    template_name = 'transport_map.html'

class SchoolsMapView(TemplateView):
    template_name = 'schools_map.html'

class SampleLetterView(TemplateView):
    template_name = 'sample_letter.html'

class ContactView(TemplateView):
    template_name = 'contact.html'

class FireView(TemplateView):
    template_name = 'fire.html'

class EditView(TemplateView):
    template_name = 'edit_letter.html'

#def home(request):
    #return render(request, 'home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    #ordering = ['-id']
    ordering = ['-post_date']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-', ' '))
    return render(request, 'categories.html', {'cats': cats.title().replace('-', ' '), 'category_posts':category_posts})

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = '__all__'
    #fields = ('title', 'body')

class AddCategoryView(CreateView):
    model = Category
    #form_class = PostForm
    template_name = 'add_category.html'
    fields = '__all__'
    #fields = ('title', 'body')

class UpdatePostView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'update_post.html'
    #fields = ['title', 'author', 'body']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
