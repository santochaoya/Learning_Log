from django.db import models

# Create your models here.
class Topic():
    """restore a topic which user is learning"""

    def __init__(self, text, time_added):
        self.text = text
        self.time_added = time_added

        text = models.CharField(max_length=200)
        time_added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        """return a string representation of the model."""

        return self.text