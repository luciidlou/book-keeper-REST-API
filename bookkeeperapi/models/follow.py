from django.db import models

class Follow(models.Model):
    sender = models.ForeignKey("Bookkeep", on_delete=models.CASCADE, related_name="sent_follow")
    receiver = models.ForeignKey("Bookkeep", on_delete=models.CASCADE, related_name="received_follow")
