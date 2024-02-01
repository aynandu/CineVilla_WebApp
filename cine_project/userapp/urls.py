from django.urls import path
from userapp import views
app_name='userapp'
urlpatterns = [
    path('register/',views.Register,name='register'),
    path('login/',views.Login,name='login'),
    path('logout/',views.Logout,name='logout'),
    path('addmovies/',views.AddMovies,name='addmovies'),
]