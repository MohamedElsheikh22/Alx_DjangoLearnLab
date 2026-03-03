from django.db import models

# Create your models here.

#Author model represents a writer who can nave multiple books
class Author(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

#Book model represents a book written by an author
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()

    #Foreignkey creates a one-to-many relationship
    #One Author > Many Books
    author = models.ForeignKey(
        Author,
        related_name='books',
        on_delete=models.CASCADE
    )
    def __str__(self):
        return self.title