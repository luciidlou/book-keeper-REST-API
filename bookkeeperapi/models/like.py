from django.db import models

class Like(models.Model):
    bookkeep = models.ForeignKey("Bookkeep", on_delete=models.CASCADE)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
