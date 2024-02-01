from django.urls import path
from cine_app import views
app_name='cine_app'
urlpatterns = [
    path('',views.allMoviedetails,name='allMoviedetails'),
    path('<slug:c_slug>/',views.allMoviedetails,name='movie_details_by_category'),
    path('<slug:c_slug>/<slug:movie_slug>/',views.detailedOfMovie,name='detailedOfMovie'),  
]