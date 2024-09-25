from django.db import models

# Create your models here.
class Author(models.Model):
    """
        It is a authors class
    """
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    age = models.IntegerField()
    
    def __str__(self):
        return self.name + "@" + str(self.age)

class Publisher(models.Model):
    """
        It is a publisher class
    """
    company = models.CharField(max_length=255)
    year = models.IntegerField()
    
    def __str__(self):
        return self.company

class Book(models.Model):
    """
        It is a books class
    """
    title = models.CharField(max_length=255)
    price = models.IntegerField()
    rating = models.IntegerField()
    published_at = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    