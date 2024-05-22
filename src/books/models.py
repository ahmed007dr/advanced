from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    bio = models.TextField()

    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author,related_name='book_author',on_delete=models.CASCADE)
    pub_date = models.DateField()
    price = models.FloatField()

    def __str__(self):
        return self.title
    
class Review(models.Model):
    book = models.ForeignKey(Book,related_name='review_book',on_delete=models.CASCADE)
    reviwer = models.CharField(max_length=100)
    feedback =  models.TextField(max_length=100)
    rating = models.IntegerField(choices=[(i,i) for i in range (1,6)])

    def __str__(self):
        return f'{str(self.book)} - {self.book}'
    
    