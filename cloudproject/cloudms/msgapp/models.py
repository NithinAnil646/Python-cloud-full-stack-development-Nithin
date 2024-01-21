# msgapp/models.py

from django.db import models

class Message(models.Model):
    sender = models.CharField(max_length=50)
    receiver = models.CharField(max_length=50)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender} to {self.receiver} - {self.timestamp}'
