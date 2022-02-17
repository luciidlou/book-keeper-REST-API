from django.db import models


class Note(models.Model):
    user_book = models.ForeignKey("UserBook", on_delete=models.CASCADE)
    content = models.CharField(max_length=500)
    datetime = models.CharField(max_length=500)
    pag_num = models.IntegerField(default=0)
