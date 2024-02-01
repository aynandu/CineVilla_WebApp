from django.shortcuts import render,get_object_or_404,redirect
from .models import Category,MovieDetails,Users
from django.core.paginator import Paginator,EmptyPage,InvalidPage
from django.contrib import messages

# Create your views here.
def allMoviedetails(request,c_slug=None):
    c_page=None
    movie_list=None
    if c_slug !=None:
        c_page=get_object_or_404(Category,slug=c_slug)
        movie_list=MovieDetails.objects.all().filter(category=c_page)
    else:
        movie_list=MovieDetails.objects.all()
    paginator=Paginator(movie_list,6)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        movies=paginator.page(page)
    except(EmptyPage,InvalidPage):
        movies=Paginator.page(paginator.num_pages)
    return render(request,'home.html',{'category':c_page,'moviedetails':movies})

def detailedOfMovie(request,c_slug,movie_slug):
    try:
        details=MovieDetails.objects.get(category__slug=c_slug,slug=movie_slug)
    except Exception as e :
        raise e
    return render(request,'details.html',{'details':details})


def Login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        
        if Users.objects.get(username=username,password=password):
            return redirect('/')
        else:
            messages.info(request,'Not a Valid User')
    return render(request,'login.html')