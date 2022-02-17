from django.db import models


class Post(models.Model):
    bookkeep = models.ForeignKey("Bookkeep", on_delete=models.CASCADE)
    shelf = models.ForeignKey("Shelf", on_delete=models.CASCADE)
    book = models.ForeignKey("Book", on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
