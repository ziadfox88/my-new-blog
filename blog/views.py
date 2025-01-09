from django.shortcuts import render,get_object_or_404,redirect
from .models import HomePage, AboutPage, ContactPage, Post
from .forms import CommentForm,ContactForm
from django.contrib import messages
# Create your views here.

def home(request):
    page= HomePage.objects.all()[0]
    posts = Post.objects.filter(status='PB')
    return render(request, 'blog/home.html',{'page':page,'posts':posts})


def about(request):
    page= AboutPage.objects.all()[0]
    return render(request, 'blog/about.html',{'page':page})   


def contact(request):
    page= ContactPage.objects.all()[0]
    massage=None
    if request.method =="POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            massage=  form.save()
            
    
    return render(request, 'blog/contact.html',{'page':page,'massage':massage})


def post_detail(request,year,month,day,post):
    post = get_object_or_404(Post,
                            status=Post.Status.PUBLISHED,
                            publish__year=year,
                            publish__month=month,
                            publish__day=day,
                            slug=post,)
    comments=post.comments.filter(active=True)
    return render(request, 'blog/post_details.html',{'post':post,"comments":comments})


def post_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)

    comment = None

    form = CommentForm(data=request.POST)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        messages.success(request,'You have made a comment ')
    #return render(request, 'blog/comment.html', {'comment': comment, 'form': form, 'post': post})
    return redirect("blog_home")


