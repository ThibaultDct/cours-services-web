from django.db import models
import uuid

class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=2048)
    isbn = models.CharField(max_length=64)

    def __str__(self):
        return "(%s) %s [%s]" % (self.isbn, self.title, self.id)

    class Meta:
        ordering = ['isbn', 'title']
