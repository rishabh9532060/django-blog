from django.shortcuts import render
from .models import Post,comment

def postlists(request):
    post=Post.objects.all()
    return render(request,'postlist.html',{'post':post})
def post_detail(request,id):
    post=Post.objects.get(id=id)
    return render(request,'post_detail.html',{'post':post})



