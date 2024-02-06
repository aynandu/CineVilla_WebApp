from django import forms
from cine_app.models import MovieDetails

class MovieForm(forms.ModelForm):
    class Meta:
        model=MovieDetails
        fields=['title','description','actors','poster','release_date','trailer_Link']