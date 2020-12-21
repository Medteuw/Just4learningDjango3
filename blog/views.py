from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author' : 'Mohamed teuw',
        'title' : 'first post',
        'date': 'December 20, 2020 - 21:36:21',
        'content' : 'this the content of the first post'
    },
    {
        'author' : 'Yeslem',
        'title' : 'Second post',
        'date': 'December 20, 2020 - 21:36:21',
        'content' : 'this the content of the second post'
    }
]

def home(request):
    context = {
        'posts' : posts,}
    
    return render(request, 'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html', {'title' : 'About'})


def contact(request):
    return render(request, 'blog/contact.html')
