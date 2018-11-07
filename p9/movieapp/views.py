from django.shortcuts import render
from .forms import movieForm
from .models import movie

def index(request):
    return render(request,'home.html')

def add_movie(request):
    form=movieForm()
    if request.method=='POST':
        form=movieForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return index(request)
    return render(request,'addmovie.html',{'form':form})

def list_movie(request):
    movie_list=movie.objects.all()
    my_dict={'movie_list':movie_list}
    return render(request,'list.html',context=my_dict)




