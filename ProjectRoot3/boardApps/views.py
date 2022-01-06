from django.shortcuts import redirect, render
from .models import Board
from django.core.paginator import Paginator
import os
from django.conf import settings

def list(request):
    page = request.GET.get('page','1')
    postlist = Board.objects.all().order_by('-id')
    paginator = Paginator(postlist, 10)
    postlist = paginator.get_page(page)
    return render(request, 'boardApps/list.html', {'postlist':postlist})

def write(request):
    if request.method == 'POST':
        #for i in range(200):
        try:
            Board.objects.create(
                names = request.POST['names'],
                passwords = request.POST['passwords'],
                titles = request.POST['titles'],
                #titles = request.POST['titles'] + "-" + str(i),
                contents = request.POST['contents'],
                mainphoto = request.FILES['mainphoto'],
            )
        except :
            Board.objects.create(
                names = request.POST['names'],
                passwords = request.POST['passwords'],
                titles = request.POST['titles'],
                #titles = request.POST['titles'] + "-" + str(i),
                contents = request.POST['contents'],
            )
        return redirect('/boardApps/list/')
    return render(request, 'boardApps/write.html')

def view(request, pk):
    postview = Board.objects.get(pk=pk)
    postview.visitcounts += 1
    postview.save()
    return render(request, 'boardApps/view.html', {'postview':postview})

def delete(request, pk):
    post = Board.objects.get(pk=pk)
    if request.method=='GET':
        post.delete()
        return redirect('../list/')
    
    
def edit(request, pk):
    post = Board.objects.get(pk=pk)
    if request.method == 'POST':
        try:
            post.titles=request.POST['titles']
            post.contents=request.POST['contents']
            post.mainphoto=request.FILES['mainphoto']
            
            print(os.path.join(settings.MEDIA_ROOT, request.POST['prevphoto']))
            os.remove(os.path.join(settings.MEDIA_ROOT,request.POST['prevphoto']))
        except:
            post.titles=request.POST['titles']
            post.contents=request.POST['contents']
        post.save()
        return redirect('../view/'+str(pk))
    else:
        return render(request, 'boardApps/edit.html', {'post':post})
    