from django.db import models
from bookkeeperapi.validators import validate_rating

class UserBook(models.Model):
    bookkeep = models.ForeignKey("Bookkeep", on_delete=models.CASCADE)
    shelf = models.ForeignKey("Shelf", on_delete=models.CASCADE)
    book = models.ForeignKey("Book", on_delete=models.CASCADE)
    date_added = models.DateField(auto_now_add=True)
    date_read = models.DateField()
    rating = models.IntegerField(validators=[validate_rating])
