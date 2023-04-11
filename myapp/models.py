from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=100)
    book_pdf = models.FileField(upload_to='pdfs/', null=True, blank=True)
    book_cover = models.ImageField(upload_to='bookcovers/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name
# Create your models here.
