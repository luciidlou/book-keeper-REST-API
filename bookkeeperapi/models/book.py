from django.db import models
from bookkeeperapi.models import UserBook

class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()
    synopsis = models.CharField(max_length=1200)
    genre = models.ForeignKey("Genre", on_delete=models.CASCADE)
    page_length = models.PositiveIntegerField()
    goodreads_link = models.URLField(max_length=200)
    image = models.ImageField(upload_to=None, height_field=None,
                              width_field=None, max_length=None, null=True)

    @property
    def average_rating(self):
        user_books = UserBook.objects.all()
        ratings = ()
        for ub in user_books:
            if ub.book == self:
                ratings.append(ub.rating)
        sum_of_ratings = sum(ratings)
        avg = sum_of_ratings / len(ratings)
        return avg