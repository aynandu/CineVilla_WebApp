from django.db import models

# Create your models here.
class Users(models.Model):
    username=models.CharField(max_length=10,unique=True)
    first_Name=models.CharField(max_length=20,unique=True)
    last_Name=models.CharField(max_length=20)
    email=models.EmailField(max_length=70)
    password=models.CharField(max_length=20)

    def __str__(self):
        return self.first_Name

class Category(models.Model):
    name=models.CharField(max_length=100,unique=True)
    slug=models.SlugField(max_length=150,unique=True)
    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'

class MovieDetails(models.Model):
    title=models.CharField(max_length=80)
    slug=models.SlugField(max_length=150,unique=True)
    poster=models.ImageField(upload_to='moviedetails',blank=True)
    description=models.CharField(max_length=250)
    release_date=models.DateField()
    actors=models.CharField(max_length=250)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    trailer_Link=models.CharField(max_length=250,blank=True)
